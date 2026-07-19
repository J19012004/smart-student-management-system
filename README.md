# 🎓 Smart Student Management System

A modern full-stack **Student Management System** built with **Django REST Framework** and **React**. The application enables educational institutions to efficiently manage student records through a secure, responsive, and intuitive web interface. It also includes a **rule-based AI Student Performance Insight System** that analyzes attendance and academic performance to identify students who may need additional support.

---

# 🚀 Features

## 🔐 Authentication
- Secure JWT Authentication (SimpleJWT)
- User Login & Logout
- Protected Routes
- Secure API Access

## 👨‍🎓 Student Management
- Add New Students
- View Student Details
- Update Student Information
- Delete Student Records
- Search Students
- Manage Student Departments
- Manage Academic Years

## 📊 Dashboard & Analytics
- Total Students Overview
- Department-wise Statistics
- Academic Year Distribution
- Interactive Charts with Chart.js
- Responsive Dashboard Cards

## 🤖 AI Student Performance Insights

The application includes a **rule-based AI recommendation engine** that evaluates student attendance and academic performance to provide useful insights.

### AI Features
- Analyze attendance percentage
- Evaluate student marks
- Predict student performance category
- Identify students requiring academic attention
- Generate simple performance recommendations

### Performance Categories
- 🟢 Excellent
- 🟡 Average
- 🟠 Needs Improvement
- 🔴 High Risk

### AI Decision Logic

```python
if attendance < 60:
    prediction = "High Risk"
elif marks < 50:
    prediction = "Needs Improvement"
elif attendance > 90 and marks > 80:
    prediction = "Excellent"
else:
    prediction = "Average"
```

> **Note:** This project uses a **rule-based AI recommendation system** for educational purposes. It demonstrates intelligent decision-making logic rather than machine learning.

## 🎨 User Interface
- Modern Responsive Design
- Bootstrap 5
- React Router Navigation
- Interactive Dashboard
- Mobile-Friendly Layout
- React Icons

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
│   ├── authentication/
│   ├── students/
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
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

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment (Windows)

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the Django development server

```bash
python manage.py runserver
```

Backend URL

```text
http://127.0.0.1:8000/
```

---

## 3. Frontend Setup

Open another terminal

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run the React development server

```bash
npm run dev
```

Frontend URL

```text
http://localhost:5173/
```

---

# 📋 Student Model

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

The application uses **JWT Authentication** with **SimpleJWT**.

After successful login:

- Access Token is generated
- Refresh Token is generated
- Protected API requests use the access token
- Secure authentication is handled through Axios

---

# 🌟 Project Highlights

- Full-Stack Web Application
- RESTful API Development
- JWT Authentication
- CRUD Operations
- Dashboard Analytics
- AI-Based Student Performance Insights
- Responsive User Interface
- Department Management
- Data Visualization with Chart.js
- MySQL Database Integration

---

# 🚀 Future Improvements

- Attendance Tracking System
- Faculty Management
- Course Management
- Student Report Generation (PDF)
- Excel Import & Export
- Email Notifications
- Role-Based Authorization
- Machine Learning-Based Performance Prediction
- Cloud Deployment (AWS, Azure, or Render)

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Django
- Django REST Framework
- React.js
- REST API Development
- JWT Authentication
- CRUD Operations
- MySQL Database
- Axios API Integration
- Chart.js
- Responsive Web Design
- AI Rule-Based Decision Systems
- Full-Stack Application Development

---

# 👨‍💻 Author

**Jerminn Rebekka M**


---

