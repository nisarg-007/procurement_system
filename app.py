import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_dbmt_project'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'procurement.db')
TMP_DB_PATH = '/tmp/procurement.db'

def get_db_connection():
    import shutil
    # Vercel serverless environment restricts file writes to /tmp/
    if os.environ.get('VERCEL') == '1':
        if not os.path.exists(TMP_DB_PATH):
            if os.path.exists(DB_PATH):
                shutil.copy2(DB_PATH, TMP_DB_PATH)
            else:
                # Fallback if somehow using wrong path
                alt_path = os.path.join(os.getcwd(), 'procurement.db')
                if os.path.exists(alt_path):
                    shutil.copy2(alt_path, TMP_DB_PATH)
        try:
            conn = sqlite3.connect(TMP_DB_PATH)
            # test if tables exist
            conn.execute("SELECT count(*) FROM Users")
        except:
            conn = sqlite3.connect(DB_PATH) # fallback
    else:
        conn = sqlite3.connect(DB_PATH)
        
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    def __init__(self, id, name, email, role_id, role_name, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.role_id = role_id
        self.role_name = role_name
        self.department_id = department_id

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('''
        SELECT u.*, r.role_name 
        FROM Users u 
        JOIN Roles r ON u.role = r.role_id 
        WHERE u.user_id = ?
    ''', (user_id,)).fetchone()
    conn.close()
    if user:
        return User(id=user['user_id'], name=user['name'], email=user['email'], 
                    role_id=user['role'], role_name=user['role_name'], department_id=user['department_id'])
    return None

from datetime import datetime
import pytz

# ... existing code ...

def log_audit(user_id, action, table_affected):
    conn = get_db_connection()
    central = pytz.timezone('US/Central')
    # Get current time in CT, formatted same way SQLite does CURRENT_TIMESTAMP (YYYY-MM-DD HH:MM:SS)
    ct_time = datetime.now(central).strftime('%Y-%m-%d %H:%M:%S')
    
    conn.execute('INSERT INTO Audit_Log (user_id, action, table_affected, ip_address, timestamp) VALUES (?, ?, ?, ?, ?)',
                 (user_id, action, table_affected, request.remote_addr, ct_time))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/api/auth', methods=['POST'])
def api_auth():
    try:
        data = request.json
        email = data.get('email')
        
        conn = get_db_connection()
        user = conn.execute('''
            SELECT u.*, r.role_name 
            FROM Users u 
            JOIN Roles r ON u.role = r.role_id 
            WHERE u.email = ?
        ''', (email,)).fetchone()
        
        if user:
            user_obj = User(id=user['user_id'], name=user['name'], email=user['email'], 
                            role_id=user['role'], role_name=user['role_name'], department_id=user['department_id'])
            login_user(user_obj)
            log_audit(user['user_id'], 'LOGIN', 'Users')
            conn.close()
            return jsonify({"success": True, "redirect": url_for('dashboard')})
        else:
            conn.close()
            return jsonify({"success": False, "error": "User email not registered in system."})
    except Exception as e:
        import traceback
        return jsonify({"success": False, "error": f"Backend Error: {str(e)}", "trace": traceback.format_exc()})

@app.route('/logout')
@login_required
def logout():
    log_audit(current_user.id, 'LOGOUT', 'Users')
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db_connection()
    data = {}
    
    if current_user.role_name == 'Employee':
        data['requests'] = conn.execute('SELECT * FROM Purchase_Requests WHERE employee_id = ? ORDER BY created_at DESC', (current_user.id,)).fetchall()
        data['kpi_total'] = len(data['requests'])
        data['kpi_approved'] = sum(1 for r in data['requests'] if r['status'] in ('APPROVED', 'PO_ISSUED'))
        data['kpi_pending'] = sum(1 for r in data['requests'] if r['status'] == 'PENDING')
    
    elif current_user.role_name == 'Manager':
        data['pending_requests'] = conn.execute('''
            SELECT * FROM Purchase_Requests 
            WHERE dept_id = ? AND status = "PENDING"
        ''', (current_user.department_id,)).fetchall()
        data['dept'] = conn.execute('SELECT * FROM Departments WHERE dept_id = ?', (current_user.department_id,)).fetchone()
        data['kpi_pending'] = len(data['pending_requests'])
        data['kpi_budget_total'] = data['dept']['budget_allocated']
        data['kpi_budget_used'] = data['dept']['budget_used']

    elif current_user.role_name == 'Procurement':
        data['approved_requests'] = conn.execute('SELECT * FROM Purchase_Requests WHERE status = "APPROVED"').fetchall()
        data['vendors'] = conn.execute('SELECT * FROM Vendors WHERE is_active = 1').fetchall()
        data['pos'] = conn.execute('SELECT po.*, v.company_name FROM Purchase_Orders po JOIN Vendors v ON po.vendor_id = v.vendor_id').fetchall()
        data['kpi_to_issue'] = len(data['approved_requests'])
        data['kpi_active'] = len(data['pos'])
        data['kpi_value'] = sum(p['total_amount'] for p in data['pos'])
        
    elif current_user.role_name == 'Vendor':
        vendor_info = conn.execute('SELECT vendor_id FROM Vendors WHERE email = ?', (current_user.email,)).fetchone()
        data['pos'] = []
        if vendor_info:
            data['pos'] = conn.execute('SELECT * FROM Purchase_Orders WHERE vendor_id = ?', (vendor_info['vendor_id'],)).fetchall()
        data['kpi_open'] = len(data['pos'])
        data['kpi_to_ship'] = sum(1 for p in data['pos'] if p['status'] == 'ISSUED')
        data['kpi_value'] = sum(p['total_amount'] for p in data['pos'])

    elif current_user.role_name == 'Finance':
        data['deliveries'] = conn.execute('SELECT gr.*, po.vendor_id FROM Goods_Receipt gr JOIN Purchase_Orders po ON gr.po_id = po.po_id WHERE po.status = "SHIPPED"').fetchall()
        data['invoices'] = conn.execute('SELECT * FROM Invoices ORDER BY invoice_id DESC').fetchall()
        data['kpi_ready'] = len(data['deliveries'])
        data['kpi_unpaid'] = sum(1 for i in data['invoices'] if i['status'] == 'PENDING')
        data['kpi_paid_amt'] = sum(i['amount'] for i in data['invoices'] if i['status'] == 'PAID')

    elif current_user.role_name == 'SuperAdmin':
        data['departments'] = conn.execute('SELECT * FROM Departments').fetchall()
        data['audit'] = conn.execute('SELECT a.*, u.email FROM Audit_Log a JOIN Users u ON a.user_id = u.user_id ORDER BY timestamp DESC LIMIT 50').fetchall()
        
        # SuperAdmin extended analytics logic
        # For simplicity, returning all POs
        data['all_pos'] = conn.execute('SELECT status, COUNT(*) as count FROM Purchase_Orders GROUP BY status').fetchall()
        data['kpi_depts'] = len(data['departments'])
        data['kpi_logs'] = sum(1 for _ in data['audit'])
        data['kpi_pos'] = sum(p['count'] for p in data['all_pos'])

    conn.close()
    return render_template('dashboard.html', data=data)

# Actions
@app.route('/submit_pr', methods=['POST'])
@login_required
def submit_pr():
    item_name = request.form['item_name']
    quantity = int(request.form['quantity'])
    cost = float(request.form['cost'])
    desc = request.form['description']
    
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO Purchase_Requests (employee_id, dept_id, item_name, description, quantity, estimated_cost)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (current_user.id, current_user.department_id, item_name, desc, quantity, cost))
    conn.commit()
    pr_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.execute('INSERT INTO PR_Status_History (pr_id, old_status, new_status, changed_by) VALUES (?, ?, ?, ?)',
                 (pr_id, 'NONE', 'PENDING', current_user.id))
    conn.commit()
    conn.close()
    
    log_audit(current_user.id, 'SUBMIT_PR', 'Purchase_Requests')
    flash('Purchase Request Submitted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/approve_pr/<int:pr_id>', methods=['POST'])
@login_required
def approve_pr(pr_id):
    decision = request.form['decision']  # 'APPROVED' or 'REJECTED'
    comments = request.form['comments']
    
    conn = get_db_connection()
    conn.execute('UPDATE Purchase_Requests SET status = ? WHERE pr_id = ?', (decision, pr_id))
    conn.execute('INSERT INTO PR_Approvals (pr_id, manager_id, decision, comments) VALUES (?, ?, ?, ?)',
                 (pr_id, current_user.id, decision, comments))
    conn.execute('INSERT INTO PR_Status_History (pr_id, old_status, new_status, changed_by) VALUES (?, ?, ?, ?)',
                 (pr_id, 'PENDING', decision, current_user.id))
    conn.commit()
    conn.close()
    log_audit(current_user.id, f'{decision}_PR', 'Purchase_Requests')
    return redirect(url_for('dashboard'))

@app.route('/generate_po', methods=['POST'])
@login_required
def generate_po():
    pr_id = request.form['pr_id']
    vendor_id = request.form['vendor_id']
    delivery_date = request.form['delivery_date']
    
    conn = get_db_connection()
    pr = conn.execute('SELECT * FROM Purchase_Requests WHERE pr_id = ?', (pr_id,)).fetchone()
    total_amt = pr['quantity'] * pr['estimated_cost']
    
    conn.execute('''
        INSERT INTO Purchase_Orders (pr_id, vendor_id, procurement_officer_id, delivery_due_date, total_amount)
        VALUES (?, ?, ?, ?, ?)
    ''', (pr_id, vendor_id, current_user.id, delivery_date, total_amt))
    conn.execute('UPDATE Purchase_Requests SET status = "PO_ISSUED" WHERE pr_id = ?', (pr_id,))
    conn.commit()
    conn.close()
    
    log_audit(current_user.id, 'GENERATE_PO', 'Purchase_Orders')
    flash('Purchase Order Generated successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/vendor_ship/<int:po_id>', methods=['POST'])
@login_required
def vendor_ship(po_id):
    conn = get_db_connection()
    conn.execute('UPDATE Purchase_Orders SET status = "SHIPPED" WHERE po_id = ?', (po_id,))
    conn.execute('INSERT INTO Goods_Receipt (po_id, received_by, quantity_received, condition_notes) VALUES (?, ?, 0, "Shipped by Vendor")', (po_id, current_user.id))
    conn.commit()
    conn.close()
    log_audit(current_user.id, 'MARK_SHIPPED', 'Purchase_Orders')
    flash('Marked as Shipped!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/finance_invoice', methods=['POST'])
@login_required
def finance_invoice():
    po_id = request.form['po_id']
    conn = get_db_connection()
    po = conn.execute('SELECT * FROM Purchase_Orders WHERE po_id = ?', (po_id,)).fetchone()
    conn.execute('INSERT INTO Invoices (po_id, vendor_id, due_date, amount) VALUES (?, ?, ?, ?)',
                 (po_id, po['vendor_id'], po['delivery_due_date'], po['total_amount']))
    conn.execute('UPDATE Purchase_Orders SET status = "INVOICED" WHERE po_id = ?', (po_id,))
    conn.commit()
    conn.close()
    log_audit(current_user.id, 'CREATE_INVOICE', 'Invoices')
    flash('Invoice Processed successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/clear_log/<int:log_id>', methods=['POST'])
@login_required
def clear_log(log_id):
    if current_user.role_name != 'SuperAdmin':
        return redirect(url_for('dashboard'))
    conn = get_db_connection()
    conn.execute('DELETE FROM Audit_Log WHERE log_id = ?', (log_id,))
    conn.commit()
    conn.close()
    flash('Audit log entry removed.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/clear_all_logs', methods=['POST'])
@login_required
def clear_all_logs():
    if current_user.role_name != 'SuperAdmin':
        return redirect(url_for('dashboard'))
    conn = get_db_connection()
    conn.execute('DELETE FROM Audit_Log')
    conn.commit()
    conn.close()
    flash('All audit logs cleared!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    from setup_db import create_database
    if not os.path.exists(DB_PATH):
        create_database()
    app.run(debug=True, port=5000)
