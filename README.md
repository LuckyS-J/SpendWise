# 💰 SpendWise – Expense Tracking Web App

**SpendWise** is a Django-based web application that allows users to track their expenses, categorize transactions, and visualize spending habits through an interactive dashboard.

---

## 🚀 Features

### 🔐 Authentication
- User registration and login via HTML forms
- Token-based authentication
- Login required for protected views

### 📦 Models
- **Category**: name and color
- **Transaction**: user, title, amount, date, category

### 🌐 API (Django REST Framework)
- `GET/POST /api/categories/` – list and create categories
- `GET/POST /api/transactions/` – list and create transactions
- `GET/PUT/DELETE /api/transactions/<id>/` – transaction details
- `GET /api/summary/` – total expenses and category breakdown

### 📊 Dashboard
- Doughnut chart for expense visualization
- Bootstrap-based UI

---

## ⚙️ Tech Stack
- Python 3, Django
- Django REST Framework
- pgSQL
- Bootstrap 5
- Chart.js

---

### 📌 Project Status
✅ Completed MVP with full CRUD functionality, dashboard, and API.
🔒 Archived for reference – being replaced by a new version focused on API design and deeper understanding of DRF.

### 👨‍💻 Learning Note
This project was built as part of my learning journey into Django and REST API development.
Many features were implemented through self-study and with the help of ChatGPT to better understand best practices and architecture.
