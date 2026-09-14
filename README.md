Live Demo Link ----->https://veerababu-class-connect.onrender.com/


🎓 Student Portal 
=================

This README is written so that anyone opening this project for the first time can understand it easily, without needing to read every line of code first.

1. What is this project?
 =====================

This is a Django (Python web framework) based "Student Portal" / Class Connect website.

In simple terms — it's a website for a coaching institute / training center:

Students can register (sign up)
Teachers can register separately
Teachers (staff members) can add / edit / delete student records
The home page shows a list of all students
On the courses page, a teacher can pick a course and see all students enrolled in it (this page is restricted to teachers only)

So basically, it's a mini Student Management System.

2. What's inside this zip file? (Folder Structure)
 ============================================
Student_Portal/
│
├── manage.py              → Django project ni run cheyadaniki main file
├── requirements.txt       → Ee project ki kavalasina Python packages list
├── populate.py            → Fake/dummy student data create cheyadaniki script
├── db.sqlite3             → Database file (ippude data store ayi undi)
│
├── Student_Portal/        → Project settings folder
│   ├── settings.py        → Django project settings (DB, apps, static files, etc.)
│   ├── urls.py             → Website lo e URL ki e page open avvalo decide chese file
│   └── wsgi.py / asgi.py  → Server deploy cheyadaniki files
│
├── testapp/                → Main app (actual logic anni idhi lone)
│   ├── models.py           → Database table structure (Student ane table)
│   ├── views.py            → Prathi page venaka unna logic (Python functions)
│   ├── forms.py            → Signup forms, Student add/edit forms
│   ├── admin.py            → Django admin panel settings
│   └── migrations/         → Database changes history
│
├── templates/               → Website HTML pages anni ikkade unnayi
│   ├── home.html            → Home page (students list)
│   ├── signup.html / studentsignup.html / teachersignup.html → Signup pages
│   ├── addstudent.html / editstudent.html → Student add/edit forms
│   ├── courses.html         → Courses page
│   ├── about.html / contact.html → Normal info pages
│   └── registration/login.html → Login page
│
└── static/                  → CSS files and images (used for website styling)
    ├── css/                 → A separate CSS file for each page
    └── images/              → Logo, icons, etc.
4. How does the main logic work?

📌 Database Table (testapp/models.py)
======================================


There's a table called Student with the following columns:

First Name, Last Name, Email
Course Name, Course Duration, Course Fees
Age
Status (Active / Completed / Enrolled)

📌 URLs (Student_Portal/urls.py)
===================================

This file defines which page opens when a particular link is clicked on the website:

URL	Page	Explanation
/	Home	Shows the list of all students
/signup/	Signup	General signup
/studentsignup/	Student Signup	For students to register
/teachersignup/	Teacher Signup	For teachers to register
/accounts/login/	Login	Login page (Django's built-in login)
/addstudent/	Add Student	Add a new student (for authorized/logged-in users)
/editstudent/<id>	Edit Student	Edit an existing student's details
/delete/<id>	Delete Student	Delete a student record (teachers/staff only)
/courses/	Courses	Pick a course and see students enrolled in it (staff only)
/about/ , /contact/	About/Contact	Regular info pages

📌 Views (testapp/views.py)
=============================

Behind every URL there's a Python function. These functions decide what should happen when a user makes a request — for example, fetching data from the database and sending it to an HTML page.

Important points:

Only teachers (users with is_staff=True) can add/edit/delete student records.
Regular/student users cannot access the courses page, delete, or edit pages — they'll see an "Access Denied" message.

📌 Forms (testapp/forms.py)
==============================

SignUpForm, StudentSignUpForm, TeacherSignUpForm → registration forms
StudentForm → form used to add/edit a student

4. How to run this project
Install requirements:
=======================
bash
   pip install -r requirements.txt
Run database migrations:
bash
   python manage.py migrate
(Optional) Add fake/dummy student data:
bash
   python manage.py shell -c "import populate"

(This needs the Faker library — install it with pip install Faker)

Start the server:
bash
   python manage.py runserver
Open in your browser:
   http://127.0.0.1:8000/
Admin panel (Django's built-in):
   http://127.0.0.1:8000/admin/

(To use this, create a superuser first: python manage.py createsuperuser)

5. Technologies used (Tech Stack)
==============================
Backend: Python + Django 5.2
Database: SQLite (data is stored in the db.sqlite3 file)
Frontend: HTML + CSS (in the templates and static folders)
Server (production): Gunicorn + Whitenoise (used to serve static files)

7. Quick Summary for Beginners
================================

This project is a coaching center management website. Students can sign up, teachers can log in and add/edit/delete student records, and students can be filtered by course. The backend runs on Django, data is stored in an SQLite database, and all the pages are HTML files inside the templates folder.

If there's any point you didn't fully understand, just ask about that specific file or function — happy to explain it in more detail! 😊
