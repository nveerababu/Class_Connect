from django.contrib import admin
from testapp.models import Student
class StudentAdmin(admin.ModelAdmin): 
    list_display = ['id', 'student_First_Name', 
                    'student_Last_Name',
                      'student_Email_Id',
                        'course_Name', 
                        'course_Duration',
                          'course_Fees' ,
                          'student_Age',
                          'status',          
                    ]
    
    list_editable = ['status']
    
    list_filter = ['status', 'course_Name']
admin.site.register(Student, StudentAdmin)  


# Register your models here.
