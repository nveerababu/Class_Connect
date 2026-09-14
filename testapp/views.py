from django.shortcuts import render
from django.contrib.auth import logout
from testapp.models import Student
from django.contrib.auth.decorators import login_required

# signup form
from testapp.forms import SignUpForm
# from django.http import HttpResponseRedirect
def signup_view(request):
    form=SignUpForm()
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         user = form.save()
#         user.set_password(user.password)
#         user.save()
#         return HttpResponseRedirect('/accounts/login')
    return render(request, 'signup.html',{'form':form})

# student signup form
from testapp.forms import StudentSignUpForm
from django.http import HttpResponseRedirect
def stdentsignup_view(request):
    form = StudentSignUpForm()
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.is_staff = False
            user.save()
            return HttpResponseRedirect('/accounts/login')  
    return render(request, 'studentsignup.html', {'form': form})


# teacher signup form
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from testapp.forms import TeacherSignUpForm
from django.http import HttpResponseRedirect
def teachersignup_view(request):
    form = TeacherSignUpForm()
    if request.method == 'POST':
            form = TeacherSignUpForm(request.POST)
            user = form.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()
            return redirect('/accounts/login/')
    return render(request, 'teachersignup.html',{'form':form})

#logout view
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')





@login_required
def courses(request):
    return render(request, 'courses.html')





#home pahe view
def home(request):
    stu_list  = Student.objects.all()
    return render(request, 'home.html', {'stu_list':stu_list} )





#add student form
from testapp.forms import StudentForm
from django.http import HttpResponseRedirect
def addstudent_view(request):
     form=StudentForm()
     if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
     return render(request, 'addstudent.html',{'form':form})


# student delete view   
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from testapp.models import Student
def delete_view(request,id):
     if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, "Access Denied: Only teachers can delete student records.")
        return redirect('/accounts/login/')
     stu  = Student.objects.get(id=id)
     stu.delete()
     return HttpResponseRedirect('/')


#student edit view
from django.shortcuts import render, redirect, get_object_or_404
from testapp.models import Student
from testapp.forms import StudentForm
def editstudent_view(request,id):
    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, "Access Denied: Only teachers can edit student records.")
        return redirect('/accounts/login/')

    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    stu  = Student.objects.get(id=id)
    form=StudentForm(instance=stu)
    if request.method== 'POST':
        form=StudentForm(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'editstudent.html',{'form':form})


#classconnect about view
def about_view(request):
    return render(request, 'about.html')

#class connect contact view
def contact_view(request):
    return render(request, 'contact.html')

#class connect courses view
from testapp.models import Student
from django.contrib import messages
from django.shortcuts import render, redirect
def courses_view(request):
    if not request.user.is_authenticated:
            messages.error(request, "Access Denied: Course details and student records are restricted to instructors only.")
            return redirect('/accounts/login/')
    if not request.user.is_staff:
            messages.error(request, "Access Denied: student records are restricted to instructors only.")
            return redirect('/accounts/login/') 
    courses = ['Python Full Stack', 'Java Full Stack', 'Data Science', 'Django', 'AWS', 'DevOps', 'React JS']
    course = request.GET.get('course')
    students = Student.objects.filter(course_Name=course) if course else None
    return render(request, 'courses.html', {'courses': courses, 'selected_course': course, 'students': students})

