from django.db import models
class Student(models.Model):
    student_First_Name = models.CharField(max_length = 150)
    student_Last_Name = models.CharField(max_length = 150)
    student_Email_Id =  models.EmailField()
    course_Name = models.CharField(max_length = 150)
    student_Age =  models.IntegerField()
    course_Duration = models.CharField(max_length=20, default='3 Months')
    course_Fees =  models.IntegerField()
       

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Enrolled', 'Enrolled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')    
    
     


# Create your models here.
