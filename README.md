# Multi-Vendor Procurement & Purchase Order Management System

## Project Overview
A fully functional, relational database-backed web application built for EDS 6343 — Database Management Tools. It models a complete end-to-end procurement lifecycle allowing enterprise users to submit, approve, and track purchase requests and purchase orders across departments through strict role-based access.

## Features & Supported Roles
We've mapped out exactly how data flows across all 5 user personas in the app:
1. **Employee:** Submits purchase requests, tracks status, views approved POs.
2. **Manager:** Views pending departmental requests, tracks department budgets, approves/rejects team requests.
3. **Procurement Officer:** Converts approved "Purchase Requests" into "Purchase Orders," selects vendors, manages vendor registry.
4. **Vendor:** Views assigned open POs, confirms acceptances, logs shipped goods.
5. **Finance Admin:** Monitors incoming deliveries, matches PO records to internal systems, processes invoices. 
6. **Super Admin:** Views real-time budget utilizations dynamically mapped to DB tables, evaluates vendor performance analytics, and oversees live audit logs.

## Technology Stack
- **Database:** SQLite3 / Full Relational Standard (22+ tables in 3NF)
- **Backend:** Python + Flask using raw parameterized SQL execution
- **Frontend:** HTML5, CSS3 Custom Properties (Neumorphism / Glassmorphism templates), Bootstrap 5 Utility classes
- **Authentication:** Dual Configuration — Internal Session Cookies + Google Firebase Identity Provider 
- **Hosting / Deployments:** Fully optimized for zero-config build on Vercel utilizing Vercel's fast `/tmp/` filesystem emulation architecture to preserve Python SQLite databases within a Serverless environment!

## Local Installation / Testing

1. Ensure Python 3.9+ is installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # (On Windows use: .venv\Scripts\activate)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Setup the database tables and insert realistic demo data:
   ```bash
   python setup_db.py
   ```
5. Run the server:
   ```bash
   python app.py
   ```
   Navigate to `http://127.0.0.1:5000` to interact with the project!

## Architecture Highlights
- Uses a centralized connection factory mapping results directly to dictionary structures (`sqlite3.Row`).
- Enforces dynamic budget checking and deduction mechanisms.
- Maintains comprehensive audit logs dynamically capturing IPs, Users, Timestamp, Actions, and Targets on all destructive actions.
