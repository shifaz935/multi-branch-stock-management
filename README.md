# 📦 Multi-Branch Stock Management System

A **role-based web application** developed using **Django** to manage products, stock levels, and price history across **multiple branches** with real-time dashboards and alerts.

---

## 📖 Project Description

The **Multi-Branch Stock Management System** helps businesses manage inventory efficiently when operating in multiple locations.

- Each branch manages its own stock
- Administrators get a **centralized view** of all branches
- Ensures data accuracy, security, and real-time monitoring

This project is designed for **real-world business use**.

---

## ⭐ Key Features

### 🔐 Role-Based Access Control
- Admin users can access all branches
- Branch users can manage stock only for their assigned branch
- Secure authentication system

### 🏬 Branch-Wise Stock Management
- Separate stock records for each branch
- Prevents unauthorized stock updates
- Easy branch-wise monitoring

### 📦 Product Management
- Add and update products
- Manage categories and pricing
- Define minimum stock level per product

### ⚠️ Low Stock Alerts
- Automatic low-stock detection
- Red warning indicators on dashboard
- Helps avoid stock shortages

### 📊 Interactive Dashboard
- Total products count
- Total stock count
- Stock level progress bars
- Branch-wise stock charts using **Chart.js**

### 💰 Price History Tracking
- Tracks old price and new price
- Stores date of price changes
- Useful for auditing and trend analysis

---

## 🛠️ Technologies Used

### Backend
- Python
- Django
- Django ORM

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript
- Chart.js

### Database
- SQLite

### Tools
- Git
- GitHub
- VS Code

---

## 🧱 System Architecture<img width="1536" height="1024" alt="system architecture" src="https://github.com/user-attachments/assets/829c792b-a83b-4c07-96c6-6116e69bbd20" />

---

## 📂 Modules Implemented

- User Authentication & Authorization
- Branch Management
- Product Management
- Stock Management
- Price History Module
- Dashboard & Data Visualization

---

## 📈 Use Cases

- Retail chains
- Warehouses
- Supermarkets
- Electronics stores
- Multi-branch businesses

---

## 🔮 Future Enhancements

- Export reports (Excel / PDF)
- Email alerts for low stock
- REST API integration
- Cloud database support
- Advanced analytics dashboard

---

## 📸 Screenshots

### Dashboard
<img width="1236" height="751" alt="dashboard" src="https://github.com/user-attachments/assets/c4a3277d-2564-46a3-aee2-f51bbadf23af" />

### Product Management

<img width="1889" height="707" alt="products" src="https://github.com/user-attachments/assets/3ccc57b6-eb6f-4b06-af6f-726130d97b2a" />
<img width="817" height="846" alt="addproduct" src="https://github.com/user-attachments/assets/865d1dad-475c-433e-bb16-8ad7a2f1e36f" />



### Stock Management
<img width="1902" height="727" alt="addstock" src="https://github.com/user-attachments/assets/0a030168-4523-4cfa-91e8-67ea475b458c" />

<img width="1892" height="717" alt="stock" src="https://github.com/user-attachments/assets/89c11506-2b7b-47f4-8526-dd66dff05dec" />

### Price History
<img width="1905" height="704" alt="price history" src="https://github.com/user-attachments/assets/259bad1a-adb8-49b7-b84e-12a4ce210dd4" />


---


## 🚀 How to Run the Project


```bash
# Clone repository<img width="817" hei<img width="1889" height="707" alt="products" src="https://github.com/user-attachments/assets/cbd541da-17ab-4086-95fe-a8c67345fe07" />
ght="846" alt="addproduct" src="https://github.com/user-attachments/assets/00d2c5f2-c9e7-489c-b6b2-d07eb222f0e7" />

git clone https://github.com/your-username/your-repo-name.git

# Activate virtual environment
venv\Scripts\activate

# Install dependencies<img width="1905" height="704" alt="product history" src="https://github.com/user-attachments/assets/6d505d4e-1e9c-43de-bd1d-f20770444e36" />
<img width="1905" height="704" alt="price history" src="https://github.com/user-attachments/assets/9b45b910-ad81-4cbc-8c85-58a0163b2f4a" />

pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver

