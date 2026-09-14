import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student_Portal.settings')
django.setup()
import  random

from testapp.models import Student
from faker import Faker
from random import *
faker = Faker()
statuses = ['Active', 'Completed', 'Enrolled']
courses = ['Python Full Stack', 'Java Full Stack', 'Data Science', 'Django', 'AWS', 'DevOps', 'React JS']
def stu(n):
    for i in range(1,n+1):
        fstudent_First_Name = faker.first_name()
        fstudent_Last_Name = faker.last_name()
        fstudent_Email_Id = faker.email()
        fcourse_Name = choice(courses)
        fcourse_Duration = faker.month()
        fcourse_Fees =randint(1000,44000)
        fstudent_Age = randint(10,22)
        fstatus = choice(statuses)
        employee_records = Student.objects.get_or_create(
        student_First_Name = fstudent_First_Name,
        student_Last_Name = fstudent_Last_Name,
        student_Email_Id = fstudent_Email_Id,
        course_Name =  fcourse_Name,
        course_Duration = fcourse_Duration,
        course_Fees = fcourse_Fees,
        student_Age = fstudent_Age,
        status =  fstatus
        )
n = int(input("Enter number of records to populate: "))
stu(n)
print(f"Successfully populated {n} student records!")