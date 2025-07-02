from django.shortcuts import render,redirect,get_object_or_404
from Course_App.models import *
from Course_App.forms import*

# Create your views here.

def home(request):
    return render(request, 'Course_App/home.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'Course_App/course_list.html', {'courses': courses})

def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = StudentForm()
    return render(request, 'course_app/student_register.html', {'form': form})

def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollments')
    else:
        form = EnrollmentForm()
    return render(request, 'Course_App/enroll_student.html', {'form': form})

def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'course')
    return render(request, 'Course_App/enrollment_list.html', {'enrollments': enrollments})

# UPDATE Student
def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('enrollments')
    else:
        form = StudentForm(instance=student)
    return render(request, 'Course_App/student_update.html', {'form': form, 'student': student})

# DELETE Student
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('enrollments')
    return render(request, 'Course_App/student_delete_confirm.html', {'student': student})