# Basic HRMS – Django Application

## Project Description
This project is a **Basic Human Resource Management System (HRMS)** developed using **Django**.  
It was built as part of the **Intern – Backend Developer assignment**.

The application covers basic HR functionalities like employee management,
attendance tracking, and simple reporting.

---

## Technologies Used
- Python
- Django
- SQLite (default Django database)
- HTML and CSS
- Git & GitHub

---

## Features Implemented

### 1. Employee Management
- Created Employee model with fields:
  - Name
  - Email
  - Address
  - Department
  - Designation
  - Date of Joining
- Employees can be added and managed using Django Admin
- Employee list is displayed on a web page

---

### 2. Attendance Tracking
- Attendance model linked to Employee
- Attendance fields:
  - Date
  - In Time
  - Out Time
- API endpoint to mark attendance
- Attendance details are shown on the employee detail page

---

### 3. Basic Reporting
- Department-wise employee count
- Implemented using Django ORM
- Displayed in table format

---

## Project Structure
- `employees/` – Contains employee and attendance logic
- `models.py` – Database models
- `views.py` – Application logic and APIs
- `urls.py` – URL routing
- `templates/` – HTML files
- `static/` – CSS styling

---

## How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/SabithaDudekula/basic-hrms-django.git

2.  Go to project folder
cd basic-hrms-django

3.  Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

4. Install Django
pip install django

5.  Run migrations
python manage.py makemigrations
python manage.py migrate

6.  Create admin user
python manage.py createsuperuser

7.  Run server
python manage.py runserver
