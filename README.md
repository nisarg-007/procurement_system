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

## 🗄 Database Schema & Visual Diagrams

The database follows a **normalized relational design** with **16 interconnected tables** across 6 functional groups. Below are professional diagrams showing every aspect of the database backbone.

---

### 📐 Diagram 1: Complete Entity-Relationship (ER) Diagram

This shows **all 16 tables**, their columns, data types, primary keys (PK), and foreign key relationships:

```mermaid
erDiagram
    Roles {
        int role_id PK
        text role_name UK
        text permissions_json
    }

    Departments {
        int dept_id PK
        text dept_name
        real budget_allocated
        real budget_used
        int manager_id FK
    }

    Users {
        int user_id PK
        text name
        text email UK
        int role FK
        int department_id FK
        timestamp created_at
        boolean is_active
    }

    Audit_Log {
        int log_id PK
        int user_id FK
        text action
        text table_affected
        timestamp timestamp
        text ip_address
    }

    Purchase_Requests {
        int pr_id PK
        int employee_id FK
        int dept_id FK
        text item_name
        text description
        int quantity
        real estimated_cost
        text status
        timestamp created_at
    }

    PR_Approvals {
        int approval_id PK
        int pr_id FK
        int manager_id FK
        text decision
        text comments
        timestamp decided_at
    }

    PR_Status_History {
        int history_id PK
        int pr_id FK
        text old_status
        text new_status
        int changed_by FK
        timestamp changed_at
    }

    Vendors {
        int vendor_id PK
        text company_name
        text contact_name
        text email
        text phone
        text address
        int rating
        boolean is_active
    }

    Vendor_Categories {
        int vc_id PK
        int vendor_id FK
        text category_name
    }

    Contracts {
        int contract_id PK
        int vendor_id FK
        text start_date
        text end_date
        text payment_terms
        real max_value
        text status
    }

    Purchase_Orders {
        int po_id PK
        int pr_id FK
        int vendor_id FK
        int procurement_officer_id FK
        timestamp issue_date
        text delivery_due_date
        text status
        real total_amount
    }

    PO_Line_Items {
        int line_id PK
        int po_id FK
        text item_description
        int quantity
        real unit_price
        real total_price
    }

    Goods_Receipt {
        int gr_id PK
        int po_id FK
        int received_by FK
        timestamp received_date
        int quantity_received
        text condition_notes
    }

    Invoices {
        int invoice_id PK
        int po_id FK
        int vendor_id FK
        timestamp invoice_date
        text due_date
        real amount
        text status
    }

    Payments {
        int payment_id PK
        int invoice_id FK
        int paid_by FK
        timestamp payment_date
        real amount_paid
        text payment_method
        text reference_no
    }

    Budget_Transactions {
        int txn_id PK
        int dept_id FK
        int po_id FK
        real amount
        text transaction_type
        timestamp recorded_at
    }

    Notifications {
        int notif_id PK
        int user_id FK
        text message
        boolean is_read
        timestamp created_at
        text link_to
    }

    Saved_Reports {
        int report_id PK
        int generated_by FK
        text report_type
        text filters_json
        timestamp generated_at
        text file_path
    }

    Roles ||--o{ Users : "defines role of"
    Departments ||--o{ Users : "employs"
    Users ||--o{ Purchase_Requests : "submits"
    Users ||--o{ Audit_Log : "generates"
    Users ||--o{ Notifications : "receives"
    Users ||--o{ Saved_Reports : "creates"
    Departments ||--o{ Purchase_Requests : "belongs to"
    Purchase_Requests ||--o{ PR_Approvals : "reviewed in"
    Purchase_Requests ||--o{ PR_Status_History : "tracked in"
    Purchase_Requests ||--o{ Purchase_Orders : "converted to"
    Vendors ||--o{ Purchase_Orders : "fulfills"
    Vendors ||--o{ Vendor_Categories : "categorized by"
    Vendors ||--o{ Contracts : "bound by"
    Vendors ||--o{ Invoices : "billed by"
    Purchase_Orders ||--o{ PO_Line_Items : "contains"
    Purchase_Orders ||--o{ Goods_Receipt : "received as"
    Purchase_Orders ||--o{ Invoices : "invoiced as"
    Purchase_Orders ||--o{ Budget_Transactions : "deducts from"
    Departments ||--o{ Budget_Transactions : "funds from"
    Invoices ||--o{ Payments : "paid via"
```

---

### 📐 Diagram 2: Table Classification by Functional Group

```mermaid
block-beta
    columns 3
    block:auth["🔐 Authentication & Identity"]:1
        Roles
        Users
        Departments
    end
    block:procure["📋 Procurement Workflow"]:1
        Purchase_Requests
        PR_Approvals
        PR_Status_History
    end
    block:vendor["🏭 Vendor & Orders"]:1
        Vendors
        Vendor_Categories
        Contracts
    end
    block:orders["📦 Order Fulfillment"]:1
        Purchase_Orders
        PO_Line_Items
        Goods_Receipt
    end
    block:finance["💰 Finance & Payments"]:1
        Invoices
        Payments
        Budget_Transactions
    end
    block:system["⚙️ System & Monitoring"]:1
        Audit_Log
        Notifications
        Saved_Reports
    end
```

---

### 📐 Diagram 3: Procurement Workflow State Machine

This shows how a Purchase Request transitions through **every possible status** across the entire system:

```mermaid
stateDiagram-v2
    [*] --> PENDING: Employee submits request
    PENDING --> APPROVED: Manager approves
    PENDING --> REJECTED: Manager rejects
    REJECTED --> [*]: End of lifecycle

    APPROVED --> PO_ISSUED: Procurement creates PO
    PO_ISSUED --> ISSUED: PO sent to Vendor

    ISSUED --> SHIPPED: Vendor marks shipped
    SHIPPED --> INVOICED: Finance creates invoice
    INVOICED --> PAID: Payment processed
    PAID --> [*]: Procurement complete

    state PENDING {
        [*] --> AwaitingReview
        AwaitingReview --> UnderReview: Manager opens
    }

    state SHIPPED {
        [*] --> GoodsReceived
        GoodsReceived --> QualityCheck: Inspect condition
        QualityCheck --> ReadyForInvoice
    }
```

---

### 📐 Diagram 4: Data Flow Diagram (DFD Level 1)

Shows how data flows between each user role, the Flask application, and the database:

```mermaid
flowchart TB
    subgraph External["👥 External Actors"]
        EMP["👤 Employee"]
        MGR["👔 Manager"]
        PROC["📋 Procurement Officer"]
        VEND["🏭 Vendor"]
        FIN["💰 Finance Team"]
        ADMIN["🛡️ Super Admin"]
    end

    subgraph App["⚙️ Flask Application Server"]
        AUTH["🔐 /api/auth\nFirebase Verify"]
        DASH["📊 /dashboard\nRole-Based Router"]
        PR_ROUTE["📝 /submit_pr\nCreate Request"]
        APR_ROUTE["✅ /approve_pr\nApprove or Reject"]
        PO_ROUTE["📦 /generate_po\nIssue Purchase Order"]
        SHIP_ROUTE["🚚 /vendor_ship\nMark Shipped"]
        INV_ROUTE["🧾 /finance_invoice\nProcess Invoice"]
        LOG_ROUTE["🗑️ /clear_log\nAudit Management"]
    end

    subgraph DB["🗄️ SQLite Database"]
        USERS_T["Users Table"]
        PR_T["Purchase_Requests"]
        PO_T["Purchase_Orders"]
        INV_T["Invoices"]
        GR_T["Goods_Receipt"]
        AUDIT_T["Audit_Log"]
        DEPT_T["Departments"]
    end

    EMP -->|"Login credentials"| AUTH
    AUTH -->|"Verify email"| USERS_T
    AUTH -->|"Session created"| DASH

    EMP -->|"Item + qty + cost"| PR_ROUTE
    PR_ROUTE -->|"INSERT"| PR_T

    MGR -->|"Decision + comment"| APR_ROUTE
    APR_ROUTE -->|"UPDATE status"| PR_T

    PROC -->|"Vendor + date"| PO_ROUTE
    PO_ROUTE -->|"INSERT"| PO_T

    VEND -->|"Confirm shipment"| SHIP_ROUTE
    SHIP_ROUTE -->|"UPDATE + INSERT"| PO_T
    SHIP_ROUTE -->|"INSERT"| GR_T

    FIN -->|"Process payment"| INV_ROUTE
    INV_ROUTE -->|"INSERT"| INV_T

    ADMIN -->|"Delete logs"| LOG_ROUTE
    LOG_ROUTE -->|"DELETE"| AUDIT_T

    DASH -->|"SELECT by role"| PR_T
    DASH -->|"SELECT by role"| PO_T
    DASH -->|"SELECT"| DEPT_T
```

---

### 📐 Diagram 5: Authentication & Login Sequence

Step-by-step sequence of how a user logs into the system:

```mermaid
sequenceDiagram
    actor User
    participant Browser as 🌐 Browser
    participant Firebase as 🔥 Firebase Auth
    participant Flask as ⚙️ Flask Backend
    participant DB as 🗄️ SQLite DB

    User->>Browser: Enter email + password
    Browser->>Firebase: signInWithEmailAndPassword()
    Firebase-->>Browser: ✅ Auth Token returned

    Browser->>Flask: POST /api/auth {email}
    Flask->>DB: SELECT FROM Users WHERE email = ?
    DB-->>Flask: User record found

    Flask->>DB: INSERT INTO Audit_Log (LOGIN)
    Flask-->>Browser: {success: true, redirect: /dashboard}
    Browser->>Flask: GET /dashboard
    Flask->>DB: SELECT role-specific data
    DB-->>Flask: Dashboard data
    Flask-->>Browser: Render dashboard.html
    Browser-->>User: 📊 Role-based dashboard displayed
```

---

### 📐 Diagram 6: Complete Procurement Lifecycle Sequence

Shows the full end-to-end journey of one purchase from request to payment:

```mermaid
sequenceDiagram
    actor Employee
    actor Manager
    actor Procurement
    actor Vendor
    actor Finance
    participant DB as 🗄️ Database

    Note over Employee,DB: PHASE 1 — REQUEST
    Employee->>DB: INSERT Purchase_Request (item, qty, cost)
    DB-->>Employee: PR created with status PENDING

    Note over Manager,DB: PHASE 2 — APPROVAL
    Manager->>DB: SELECT pending PRs for department
    DB-->>Manager: List of pending requests
    Manager->>DB: UPDATE PR status = APPROVED
    Manager->>DB: INSERT PR_Approval (decision, comments)
    Manager->>DB: INSERT PR_Status_History

    Note over Procurement,DB: PHASE 3 — PURCHASE ORDER
    Procurement->>DB: SELECT approved PRs
    DB-->>Procurement: Approved requests list
    Procurement->>DB: INSERT Purchase_Order (vendor, date, amount)
    Procurement->>DB: UPDATE PR status = PO_ISSUED

    Note over Vendor,DB: PHASE 4 — FULFILLMENT
    Vendor->>DB: SELECT POs for vendor_id
    DB-->>Vendor: Assigned orders
    Vendor->>DB: UPDATE PO status = SHIPPED
    Vendor->>DB: INSERT Goods_Receipt

    Note over Finance,DB: PHASE 5 — PAYMENT
    Finance->>DB: SELECT shipped Goods_Receipts
    DB-->>Finance: Receipts ready for invoice
    Finance->>DB: INSERT Invoice (amount, due_date)
    Finance->>DB: UPDATE PO status = INVOICED

    Note over Employee,DB: ✅ PROCUREMENT CYCLE COMPLETE
```

---

### 📐 Diagram 7: Database Normalization Analysis

The schema satisfies **Third Normal Form (3NF)** — here's the breakdown:

| Normal Form | Requirement | How Our Schema Satisfies It |
|-------------|-------------|-----------------------------|
| **1NF** | All columns atomic, no repeating groups | ✅ Every column stores a single value. No arrays or nested data. |
| **2NF** | No partial dependencies on composite keys | ✅ All tables use single-column `AUTOINCREMENT` primary keys, eliminating partial dependencies entirely. |
| **3NF** | No transitive dependencies | ✅ Non-key attributes depend only on the PK. Example: `Users.role` → `Roles` table (not stored redundantly). Budget data lives in `Departments`, not duplicated in `Users`. |

**Key Normalization Decisions:**
- **Roles** separated from **Users** → avoids storing role names repeatedly
- **Departments** separated from **Users** → budget data stored once, not per-user
- **PR_Approvals** separated from **Purchase_Requests** → one PR can have multiple review records
- **PR_Status_History** tracks every state change independently → full audit trail
- **Vendor_Categories** separated from **Vendors** → one vendor can serve multiple categories (1:N)
- **PO_Line_Items** separated from **Purchase_Orders** → one PO can contain multiple items
- **Budget_Transactions** separated from **Departments** → transaction log vs. running total

### Foreign Key Dependency Map

```mermaid
flowchart LR
    Roles -->|role_id| Users
    Departments -->|dept_id| Users
    Users -->|user_id| Purchase_Requests
    Users -->|user_id| Audit_Log
    Users -->|user_id| Notifications
    Users -->|user_id| Saved_Reports
    Departments -->|dept_id| Purchase_Requests
    Purchase_Requests -->|pr_id| PR_Approvals
    Purchase_Requests -->|pr_id| PR_Status_History
    Purchase_Requests -->|pr_id| Purchase_Orders
    Vendors -->|vendor_id| Purchase_Orders
    Vendors -->|vendor_id| Vendor_Categories
    Vendors -->|vendor_id| Contracts
    Purchase_Orders -->|po_id| PO_Line_Items
    Purchase_Orders -->|po_id| Goods_Receipt
    Purchase_Orders -->|po_id| Invoices
    Purchase_Orders -->|po_id| Budget_Transactions
    Departments -->|dept_id| Budget_Transactions
    Invoices -->|invoice_id| Payments
    Vendors -->|vendor_id| Invoices
```

---

### 📐 Diagram 8: Use Case Diagram

Shows which actions each user role can perform in the system:

```mermaid
flowchart TB
    subgraph System["🏢 Procurement Management System"]
        UC1["📝 Submit Purchase Request"]
        UC2["📊 View Request History"]
        UC3["✅ Approve/Reject Request"]
        UC4["💰 View Department Budget"]
        UC5["📦 Generate Purchase Order"]
        UC6["🏭 Select Vendor"]
        UC7["🚚 Mark Order Shipped"]
        UC8["🧾 Process Invoice"]
        UC9["📈 View Accounts Payable"]
        UC10["📊 View Budget Charts"]
        UC11["📋 View Audit Logs"]
        UC12["🗑️ Clear Audit Logs"]
        UC13["📊 View PO Pipeline Chart"]
        UC14["📊 View KPI Metrics"]
    end

    EMP["👤 Employee"] --> UC1
    EMP --> UC2
    EMP --> UC14

    MGR["👔 Manager"] --> UC3
    MGR --> UC4
    MGR --> UC14

    PROC["📋 Procurement"] --> UC5
    PROC --> UC6
    PROC --> UC14

    VEND["🏭 Vendor"] --> UC7
    VEND --> UC14

    FIN["💰 Finance"] --> UC8
    FIN --> UC9
    FIN --> UC14

    ADMIN["🛡️ Super Admin"] --> UC10
    ADMIN --> UC11
    ADMIN --> UC12
    ADMIN --> UC13
    ADMIN --> UC14
```

---

### All 16 Tables Summary

| # | Table | Group | PK | Foreign Keys | Purpose |
|---|-------|-------|----|-------------|---------|
| 1 | **Roles** | Auth | `role_id` | — | System role definitions |
| 2 | **Users** | Auth | `user_id` | `role`, `department_id` | User accounts |
| 3 | **Departments** | Auth | `dept_id` | `manager_id` | Budget tracking per department |
| 4 | **Audit_Log** | System | `log_id` | `user_id` | Action logging with IP & timestamp |
| 5 | **Purchase_Requests** | Workflow | `pr_id` | `employee_id`, `dept_id` | Item requests from employees |
| 6 | **PR_Approvals** | Workflow | `approval_id` | `pr_id`, `manager_id` | Manager review decisions |
| 7 | **PR_Status_History** | Workflow | `history_id` | `pr_id`, `changed_by` | Status change audit trail |
| 8 | **Vendors** | Vendor | `vendor_id` | — | Supplier companies |
| 9 | **Vendor_Categories** | Vendor | `vc_id` | `vendor_id` | Vendor specializations |
| 10 | **Contracts** | Vendor | `contract_id` | `vendor_id` | Vendor agreements |
| 11 | **Purchase_Orders** | Orders | `po_id` | `pr_id`, `vendor_id`, `officer_id` | Official purchase documents |
| 12 | **PO_Line_Items** | Orders | `line_id` | `po_id` | Individual items within a PO |
| 13 | **Goods_Receipt** | Orders | `gr_id` | `po_id`, `received_by` | Delivery confirmation records |
| 14 | **Invoices** | Finance | `invoice_id` | `po_id`, `vendor_id` | Billing documents |
| 15 | **Payments** | Finance | `payment_id` | `invoice_id`, `paid_by` | Payment transactions |
| 16 | **Budget_Transactions** | Finance | `txn_id` | `dept_id`, `po_id` | Department budget movements |
| — | **Notifications** | System | `notif_id` | `user_id` | User notifications |
| — | **Saved_Reports** | System | `report_id` | `generated_by` | Exported report records |

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
