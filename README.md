# 🎓 Smart Student Management System

A modern full-stack **Student Management System** built using **Django REST Framework** and **React**. The application helps educational institutions manage student records efficiently through a secure and user-friendly dashboard.

---

## 🚀 Features

### 🔐 Authentication
- Secure JWT Authentication
- User Login & Logout
- Protected Routes
- Secure API Access

### 👨‍🎓 Student Management
- Add New Students
- View Student Details
- Update Student Information
- Delete Student Records
- Search Students
- Manage Department and Academic Year

### 📊 Dashboard
- Total Students Overview
- Department-wise Statistics
- Year-wise Student Distribution
- Interactive Charts using Chart.js
- Responsive Dashboard Cards

### 🤖 Student Performance Insights
A rule-based student performance analysis system that classifies students based on attendance and marks into:
- Excellent
- Average
- Needs Improvement
- High Risk

### 🎨 Responsive User Interface
- Bootstrap 5
- Mobile-Friendly Design
- React Router Navigation
- Modern Dashboard Layout
- Interactive Icons

---

# 🛠️ Tech Stack

## Backend
- Django
- Django REST Framework
- MySQL
- JWT Authentication (SimpleJWT)
- Python

## Frontend
- React (Vite)
- Bootstrap 5
- Axios
- React Router DOM
- Chart.js
- React Icons

---

# 📂 Project Structure

```text
student-management-system/
│
├── backend/
│   ├── students/
│   ├── authentication/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── assets/
│   │   └── App.jsx
│   └── package.json
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system.git
```

```bash
cd student-management-system
```

---

## 2. Backend Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the Django server:

```bash
python manage.py runserver
```

Backend runs at:

```text
http://127.0.0.1:8000/
```

---

## 3. Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the React application:

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173/
```

---

# 📊 Student Model

```python
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    address = models.TextField()
```

---

# 🔐 Authentication

The project uses **JWT Authentication** with **SimpleJWT**.

After a successful login:
- Access Token is generated.
- Refresh Token is generated.
- Protected API requests are authenticated using the access token.

---

# 🌱 Future Improvements

- Attendance Management
- Course Management
- Faculty Management
- PDF Report Generation
- Excel Import & Export
- Email Notifications
- Role-Based Authorization
- AI-powered Student Performance Prediction
- Cloud Deployment

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Django REST Framework
- React.js
- REST API Development
- JWT Authentication
- CRUD Operations
- MySQL Database
- Axios API Integration
- Chart.js Visualization
- Responsive Web Design
- Full-Stack Application Development

---

# 👨‍💻 Author

**Jerminn Rebekka M**
