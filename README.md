Live Demo Link ----->https://veerababu-class-connect.onrender.com/


 Student Portal:
 =================

This README is written so that anyone opening this project for the first time can understand it easily, without needing to read every line of code first.



 What is this project?
 =====================

This is a Django (Python web framework) based "Student Portal" / Class Connect website.

In simple terms — it's a website for a coaching institute / training center:
- Students can register (sign up)
- Teachers can register separately
- Teachers (staff members) can add / edit / delete student records
- The home page shows a list of all students
- On the courses page, a teacher can pick a course and see all students enrolled in it (this page is restricted to teachers only)

So basically, it's a mini Student Management System.

---

Folder Structure:
=================

Student_Portal/
│
├── manage.py              → Main file to run the Django project
├── requirements.txt       → List of Python packages needed for this project
├── populate.py            → Script to create fake/dummy student data
├── db.sqlite3             → Database file (this is where data is stored)
│
├── Student_Portal/        → Project settings folder
│   ├── settings.py        → Django project settings (DB, apps, static files, etc.)
│   ├── urls.py            → File that decides which page opens for which URL
│   └── wsgi.py / asgi.py  → Files used to deploy the server
│
├── testapp/               → Main app (all the actual logic lives here)
│   ├── models.py          → Database table structure (the "Student" table)
│   ├── views.py           → Logic behind each page (Python functions)
│   ├── forms.py           → Signup forms, student add/edit forms
│   ├── admin.py           → Django admin panel settings
│   └── migrations/        → History of database changes
│
├── templates/              → All the website's HTML pages are here
│   ├── home.html           → Home page (list of students)
│   ├── signup.html / studentsignup.html / teachersignup.html → Signup pages
│   ├── addstudent.html / editstudent.html → Student add/edit forms
│   ├── courses.html        → Courses page
│   ├── about.html / contact.html → Regular info pages
│   └── registration/login.html → Login page
│
└── static/                 → CSS files and images (used for website styling)
    ├── css/                → A separate CSS file for each page
    └── images/             → Logo, icons, etc.

---

 How does the main logic work?
 ===============================

Database Table (testapp/models.py)
==============================
There's a table called Student with the following columns:
- First Name, Last Name, Email
- Course Name, Course Duration, Course Fees
- Age
- Status (Active / Completed / Enrolled)
- 
 URLs (Student_Portal/urls.py)
=================================
This file defines which page opens when a particular link is clicked on the website:

- /                    → Home: Shows the list of all students
- /signup/             → Signup: General signup
- /studentsignup/      → Student Signup: For students to register
- /teachersignup/      → Teacher Signup: For teachers to register
- /accounts/login/     → Login: Login page (Django's built-in login)
- /addstudent/         → Add Student: Add a new student (for authorized/logged-in users)
- /editstudent/<id>    → Edit Student: Edit an existing student's details
- /delete/<id>         → Delete Student: Delete a student record (teachers/staff only)
- /courses/            → Courses: Pick a course and see students enrolled in it (staff only)
- /about/ , /contact/  → About/Contact: Regular info pages

Views (testapp/views.py)
========================
Behind every URL there's a Python function. These functions decide what should happen when a user makes a request — for example, fetching data from the database and sending it to an HTML page.

Important points:
- Only teachers (users with is_staff=True) can add/edit/delete student records.
- Regular/student users cannot access the courses page, delete, or edit pages — they'll see an "Access Denied" message.

 Forms (testapp/forms.py)
 =======================
- SignUpForm, StudentSignUpForm, TeacherSignUpForm → registration forms
- StudentForm → form used to add/edit a student

---

 How to run this project
 =======================

1. Install requirements:
   pip install -r requirements.txt

2. Run database migrations:
   python manage.py migrate

3. (Optional) Add fake/dummy student data:
   python manage.py shell -c "import populate"
   (This needs the Faker library — install it with: pip install Faker)

4. Start the server:
   python manage.py runserver

5. Open in your browser:
   http://127.0.0.1:8000/

6. Admin panel (Django's built-in):
   http://127.0.0.1:8000/admin/
   (To use this, create a superuser first: python manage.py createsuperuser)

---

 Technologies used (Tech Stack)
 ===========================

- Backend: Python + Django 5.2
- Database: SQLite (data is stored in the db.sqlite3 file)
- Frontend: HTML + CSS (in the templates and static folders)
- Server (production): Gunicorn + Whitenoise (used to serve static files)

---

 Quick Summary for Beginners
 ==========================

This project is a coaching center management website. Students can sign up, teachers can log in and add/edit/delete student records, and students can be filtered by course. The backend runs on Django, data is stored in an SQLite database, and all the pages are HTML files inside the templates folder.



If there's any point you didn't fully understand, just ask about that specific file or function — happy to explain it in more detail!
