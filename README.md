# 🏢 Multi-Vendor Procurement & Purchase Order Management System

> A full-stack, role-based enterprise procurement platform built with Python Flask, SQLite, Firebase Authentication, and deployed live on Vercel.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Vercel-black?style=for-the-badge)](https://procurement-system-peach.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-green?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![Firebase](https://img.shields.io/badge/Firebase-Auth-orange?style=flat-square&logo=firebase)](https://firebase.google.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite)](https://sqlite.org)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [Database Schema (ER Design)](#-database-schema-er-design)
- [User Roles & Workflow](#-user-roles--workflow)
- [KPI Dashboards](#-kpi-dashboards)
- [Screenshots](#-screenshots)
- [Installation & Setup](#-installation--setup)
- [Deployment on Vercel](#-deployment-on-vercel)
- [Project Structure](#-project-structure)
- [Test Accounts](#-test-accounts)
- [Security Features](#-security-features)
- [Author](#-author)

---

## 🎯 Project Overview

This project simulates a **real-world enterprise procurement workflow** — the complete lifecycle of how an organization purchases goods from external vendors. It covers every step from an employee requesting an item, through managerial approval, vendor selection, purchase order generation, shipment tracking, invoice processing, and financial payment.

The system is designed for **users of all technical backgrounds** — each role sees only what they need, with clear KPI metrics displayed as large, color-coded number cards at the top of every dashboard for instant situational awareness.

### Business Problem Solved

In large organizations, procurement is a multi-step, multi-department process involving:
- **Employees** who need to request items
- **Managers** who approve or reject requests based on budgets
- **Procurement Officers** who find vendors and issue Purchase Orders
- **Vendors** who fulfill and ship orders
- **Finance Teams** who process invoices and release payments
- **Administrators** who oversee the entire operation

This system digitizes and streamlines this entire pipeline with role-based access control, real-time budget tracking, audit logging, and data visualization.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔐 **Firebase Authentication** | Secure email/password login via Google Firebase Auth SDK |
| 👥 **6 User Roles** | Employee, Manager, Procurement, Vendor, Finance, Super Admin |
| 📊 **KPI Dashboard Cards** | Real-time metrics displayed as large, easy-to-read number cards for every role |
| 📈 **Chart.js Visualizations** | Interactive doughnut and pie charts for budget analysis and order pipeline |
| 💰 **Budget Tracking** | Real-time department budget allocation, usage, and remaining balance |
| 📝 **Full Audit Trail** | Every action logged with timestamp (Central Time), user, IP address |
| 🗑️ **Admin Log Management** | Super Admin can clear logs individually or wipe all at once |
| 🎨 **Premium Dark UI** | Glassmorphism cards, gradient backgrounds, animated blobs, hover effects |
| ☁️ **Vercel Deployment** | Live serverless deployment with automatic GitHub CI/CD |
| 📱 **Responsive Design** | Works on desktop, tablet, and mobile screens |

---

## 🛠 Technology Stack

### Backend
| Technology | Purpose |
|-----------|---------|
| **Python 3.12** | Core programming language |
| **Flask 3.0.2** | Lightweight web framework for routing, templates, and request handling |
| **Flask-Login 0.6.3** | Session management and user authentication state |
| **SQLite 3** | Embedded relational database — zero configuration, file-based |
| **pytz** | Timezone handling — all audit logs recorded in US/Central time |

### Frontend
| Technology | Purpose |
|-----------|---------|
| **HTML5 / Jinja2** | Page structure and server-side template rendering |
| **CSS3 (Custom)** | Dark theme, glassmorphism, gradients, blob animations |
| **Bootstrap 5.3** | Responsive grid system, tables, badges, progress bars |
| **JavaScript (ES6+)** | Client-side Firebase auth, dynamic chart rendering |
| **Chart.js 4.x** | Interactive doughnut and pie chart visualizations |
| **Google Fonts (Inter)** | Modern, clean typography |

### Authentication
| Technology | Purpose |
|-----------|---------|
| **Firebase Auth SDK** | Client-side email/password authentication |
| **Firebase Console** | User management, API key restrictions by domain |

### Deployment & DevOps
| Technology | Purpose |
|-----------|---------|
| **Vercel** | Serverless Python hosting with automatic GitHub deploys |
| **GitHub** | Version control and CI/CD trigger |
| **Git** | Source code management |

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      USER BROWSER                       │
│                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────┐  │
│  │ Login Page   │───▶│ Firebase Auth│───▶│ Dashboard │  │
│  │ (HTML/JS)    │    │ (Client SDK) │    │ (Jinja2)  │  │
│  └──────────────┘    └──────┬───────┘    └─────┬─────┘  │
└─────────────────────────────┼──────────────────┼────────┘
                              │                  │
                    ┌─────────▼──────────────────▼────────┐
                    │         FLASK BACKEND (app.py)       │
                    │                                      │
                    │  /api/auth ◄── Firebase email verify │
                    │  /dashboard ◄── Role-based routing   │
                    │  /submit_pr ◄── Create requests      │
                    │  /approve_pr ◄── Manager decisions   │
                    │  /generate_po ◄── Issue orders       │
                    │  /vendor_ship ◄── Mark shipped       │
                    │  /finance_invoice ◄── Process pays   │
                    │  /clear_log ◄── Admin log control    │
                    │  /clear_all_logs ◄── Bulk wipe       │
                    └─────────────────┬────────────────────┘
                                      │
                    ┌─────────────────▼────────────────────┐
                    │        SQLite DATABASE                │
                    │        (procurement.db)               │
                    │                                      │
                    │  Tables: Users, Roles, Departments,  │
                    │  Vendors, Purchase_Requests,         │
                    │  PR_Approvals, PR_Status_History,     │
                    │  Purchase_Orders, Goods_Receipt,     │
                    │  Invoices, Payments, Audit_Log       │
                    └──────────────────────────────────────┘
```

---

## 🗄 Database Schema (ER Design)

The database follows a **normalized relational design** with 12 interconnected tables:

### Core Tables

| Table | Primary Key | Purpose |
|-------|-------------|---------|
| **Roles** | `role_id` | Defines system roles (Employee, Manager, etc.) |
| **Users** | `user_id` | Stores user accounts with FK to Roles and Departments |
| **Departments** | `dept_id` | Tracks department names, budgets allocated & used |
| **Vendors** | `vendor_id` | External supplier companies with ratings |

### Workflow Tables

| Table | Primary Key | Purpose |
|-------|-------------|---------|
| **Purchase_Requests** | `pr_id` | Employee-submitted item requests with status tracking |
| **PR_Approvals** | `approval_id` | Manager approval/rejection decisions with comments |
| **PR_Status_History** | `history_id` | Complete status change audit trail for every PR |
| **Purchase_Orders** | `po_id` | Official orders issued to vendors with amounts and dates |
| **Goods_Receipt** | `gr_id` | Records of received shipments with condition notes |
| **Invoices** | `invoice_id` | Financial invoices generated from completed deliveries |
| **Payments** | `payment_id` | Payment records against invoices |

### System Tables

| Table | Primary Key | Purpose |
|-------|-------------|---------|
| **Audit_Log** | `log_id` | Every user action logged with timestamp, IP, and target table |

### Key Relationships
```
Users ──────┬──── belongs to ────▶ Departments
            ├──── has role ───────▶ Roles
            └──── submits ────────▶ Purchase_Requests
                                        │
                                   approved by
                                        │
                                        ▼
                                   PR_Approvals ──▶ Purchase_Orders
                                                        │
                                                   fulfilled by
                                                        │
                                                        ▼
                                                   Goods_Receipt ──▶ Invoices ──▶ Payments
```

---

## 👥 User Roles & Workflow

### Complete Procurement Lifecycle

```
Step 1          Step 2          Step 3           Step 4          Step 5           Step 6
┌─────────┐    ┌─────────┐    ┌────────────┐   ┌─────────┐    ┌─────────┐     ┌─────────┐
│EMPLOYEE │───▶│MANAGER  │───▶│PROCUREMENT │──▶│ VENDOR  │───▶│FINANCE  │────▶│  PAID   │
│ Submit  │    │ Approve │    │ Issue PO   │   │  Ship   │    │ Invoice │     │  ✅     │
│ Request │    │/Reject  │    │ + Vendor   │   │ Goods   │    │ Process │     │         │
└─────────┘    └─────────┘    └────────────┘   └─────────┘    └─────────┘     └─────────┘
```

### Role-by-Role Breakdown

#### 1. 👤 Employee
- **What they do:** Submit purchase requests for items they need
- **What they see:** A form to create requests + their complete request history
- **KPI Cards:** Total Requests | Approved Count | Pending Count
- **Visualization:** Doughnut chart showing approval vs. rejection ratio

#### 2. 👔 Manager
- **What they do:** Review and approve/reject purchase requests from their department
- **What they see:** Pending requests with approve/reject buttons, department budget status
- **KPI Cards:** Pending Approvals | Total Budget | Budget Used
- **Controls:** Must provide a review comment with every decision

#### 3. 📋 Procurement Officer
- **What they do:** Convert approved requests into official Purchase Orders by selecting a vendor
- **What they see:** Approved requests ready for PO generation + active PO pipeline
- **KPI Cards:** Requests To Issue | Active Pipeline | Total Pipeline Value
- **Controls:** Vendor selection dropdown with ratings, delivery date picker

#### 4. 🏭 Vendor
- **What they do:** View assigned purchase orders and mark them as shipped
- **What they see:** Their open orders with values and due dates
- **KPI Cards:** Total Orders | Pending Shipment | Contracted Value
- **Controls:** "Mark Shipped" button for each issued PO

#### 5. 💰 Finance
- **What they do:** Process invoices for shipped goods and track payments
- **What they see:** Pending goods receipts + accounts payable ledger
- **KPI Cards:** Ready for Invoice | Unpaid Invoices | Capital Paid Out
- **Controls:** "Process Invoice" button for each shipped receipt

#### 6. 🛡️ Super Admin
- **What they do:** Monitor the entire system — budgets, orders, audit trail
- **What they see:** Department budgets chart, PO pipeline chart, full audit log
- **KPI Cards:** Operating Departments | Total Issued POs | Recorded Audit Events
- **Controls:** Delete individual log entries or clear all logs at once
- **Charts:** Department Budget Doughnut + PO Status Pipeline Pie Chart

---

## 📊 KPI Dashboards

Every role's dashboard starts with **3 Key Performance Indicator (KPI) cards** — large, color-coded numbers that give instant insight without requiring any technical knowledge:

| Role | KPI 1 | KPI 2 | KPI 3 |
|------|-------|-------|-------|
| **Employee** | Total Requests (white) | Approved (green) | Pending (gray) |
| **Manager** | Pending Approvals (white) | Total Budget (green) | Budget Used (red) |
| **Procurement** | To Issue (blue) | Active Pipeline (green) | Pipeline Value (yellow) |
| **Vendor** | Total Orders (white) | Pending Shipment (yellow) | Contracted Value (green) |
| **Finance** | Ready for Invoice (blue) | Unpaid (yellow) | Capital Paid (green) |
| **Super Admin** | Departments (blue) | Total POs (blue) | Audit Events (gray) |

---

## 🖥 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Local Development

```bash
# 1. Clone the repository
git clone https://github.com/nisarg-007/procurement_system.git
cd procurement_system

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
```

The app will start at **http://127.0.0.1:5000**

> **Note:** The database (`procurement.db`) is pre-populated with test users, departments, vendors, and sample procurement data. If you need to reset it, delete the file and run `python setup_db.py` followed by `python populate_db.py`.

---

## ☁️ Deployment on Vercel

The application is deployed as a **serverless Python function** on Vercel:

1. **`vercel.json`** configures the build to use `@vercel/python` runtime
2. **All routes** (`/(.*)`) are forwarded to `app.py`
3. **Database handling:** Since Vercel's filesystem is read-only, the app copies `procurement.db` to `/tmp/` on first request
4. **CI/CD:** Every `git push` to the `master` branch triggers an automatic Vercel redeploy

### Environment Detection
```python
if os.environ.get('VERCEL') == '1':
    # Use /tmp/ for database operations
else:
    # Use local procurement.db directly
```

---

## 📁 Project Structure

```
procurement_system/
├── app.py                  # Main Flask application (routes, auth, logic)
├── setup_db.py             # Database schema creation & initial seed data
├── populate_db.py          # Dummy data generator (15+ realistic entries)
├── procurement.db          # SQLite database file (pre-populated)
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment configuration
├── .gitignore              # Git exclusions
├── README.md               # This file
│
├── static/
│   └── style.css           # Custom CSS (dark theme, glassmorphism, animations)
│
└── templates/
    ├── base.html            # Base layout (navbar, background blobs, scripts)
    ├── login.html           # Firebase authentication login page
    └── dashboard.html       # Role-based dashboard (all 6 roles in one template)
```

---

## 🔑 Test Accounts

All accounts use the password: **`test123`**

| Email | Role | Access Level |
|-------|------|-------------|
| `employee@test.com` | Employee | Submit purchase requests |
| `manager@test.com` | Manager | Approve/reject requests, view budget |
| `procurement@test.com` | Procurement | Issue POs, manage vendor pipeline |
| `vendor@test.com` | Vendor | View orders, mark shipments |
| `finance@test.com` | Finance | Process invoices, track payments |
| `admin@test.com` | Super Admin | Full system oversight, log management |

---

## 🔒 Security Features

| Feature | Implementation |
|---------|---------------|
| **Authentication** | Firebase Auth SDK (client-side) + Flask-Login (server-side sessions) |
| **API Key Restrictions** | Firebase API keys restricted to `127.0.0.1:5000` and `*.vercel.app` domains |
| **Role-Based Access** | Each route checks `current_user.role_name` before serving data |
| **CSRF Protection** | Flask session-based with secret key |
| **Audit Logging** | Every login, logout, and data mutation is recorded with IP and timestamp |
| **Timezone Consistency** | All timestamps recorded in US/Central timezone via `pytz` |
| **Input Validation** | Server-side form validation on all POST routes |
| **Admin Controls** | Only SuperAdmin role can access log deletion endpoints |

---

## 🧪 Tools & Technologies Summary

```
Backend Framework ......... Flask 3.0.2 (Python)
Database .................. SQLite 3 (embedded, file-based)
Authentication ............ Firebase Auth (Email/Password)
Session Management ........ Flask-Login 0.6.3
Timezone Handling ......... pytz (US/Central)
Frontend Framework ........ Bootstrap 5.3.3
Charting Library .......... Chart.js 4.x
Template Engine ........... Jinja2 (bundled with Flask)
Typography ................ Google Fonts (Inter)
Deployment Platform ....... Vercel (serverless Python)
Version Control ........... Git + GitHub
CI/CD .................... Vercel GitHub Integration (auto-deploy on push)
Design Language ........... Dark theme, Glassmorphism, CSS animations
```

---

## 👨‍💻 Author

**Nisarg Shah**
- GitHub: [@nisarg-007](https://github.com/nisarg-007)
- Course: Database Management (DBMT) — Semester 2

---

> *Built as a comprehensive database management project demonstrating relational database design, normalized schema architecture, role-based access control, and full-stack web development.*
