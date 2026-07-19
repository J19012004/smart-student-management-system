🎓 Smart Student Management System

A full-stack Student Management System built with Django REST Framework and React. The application enables educational institutions to manage student records efficiently through a modern dashboard with secure authentication, analytics, and CRUD operations.

📌 Features
🔐 Authentication
JWT-based authentication (SimpleJWT)
Secure login and logout
Protected API endpoints
Role-based access ready
👨‍🎓 Student Management
Add new students
View student details
Update student information
Delete student records
Search students
Department-wise organization
📊 Dashboard & Analytics
Total students overview
Department statistics
Year-wise distribution
Interactive charts using Chart.js
Responsive dashboard cards
🤖 Student Performance Insights

A rule-based recommendation engine that evaluates student attendance and marks to classify students into categories such as:

Excellent
Average
Needs Improvement
High Risk

This demonstrates backend decision logic without relying on machine learning.

🎨 Modern UI
Responsive Bootstrap 5 interface
Clean dashboard layout
React Router navigation
React Icons integration
Mobile-friendly design
🛠️ Tech Stack
Backend
Django
Django REST Framework
JWT Authentication (SimpleJWT)
MySQL
Python
Frontend
React (Vite)
Bootstrap 5
Axios
React Router DOM
Chart.js
React Icons
📂 Project Structure
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
🚀 Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/student-management-system.git
cd student-management-system
2️⃣ Backend Setup

Create a virtual environment:

python -m venv venv

Activate it (Windows):

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py makemigrations
python manage.py migrate

Start the backend:

python manage.py runserver

Backend URL:

http://127.0.0.1:8000/
3️⃣ Frontend Setup

Open a new terminal:

cd frontend

Install dependencies:

npm install

Run the React application:

npm run dev

Frontend URL:

http://localhost:5173/

📊 Student Model
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
🔒 Authentication

JWT authentication is implemented using SimpleJWT.

Access and refresh tokens are issued on login and attached to authenticated API requests using Axios.

📈 Future Enhancements
Student attendance management
Course management
Faculty management
PDF report generation
Email notifications
Excel import/export
Role-based permissions
Cloud deployment
AI-powered student performance prediction using machine learning
📚 Learning Outcomes

This project demonstrates practical experience with:

Django REST Framework API development
React frontend development
RESTful API integration
JWT authentication
CRUD operations
Database management with MySQL
Dashboard development
State management
Responsive UI design
Full-stack application architecture
