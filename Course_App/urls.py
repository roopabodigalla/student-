"""
URL configuration for Course_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Course_App.views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('course_list/',course_list,name='course_list'),
    path('student_register/',student_register,name='student_register'),
    path('enroll_student/',enroll_student,name='enroll_student'),
    path('enrollments/',enrollment_list,name='enrollments'),
    path('student_update/<int:student_id>/',student_update, name='student_update'),
    path('student_delete/<int:student_id>/',student_delete, name='student_delete'),
    
]
