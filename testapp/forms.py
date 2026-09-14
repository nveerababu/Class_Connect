from django import forms 
from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name' ]
class StudentSignUpForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name' ]
class TeacherSignUpForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name' ]

from testapp.models import Student
class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = '__all__'
