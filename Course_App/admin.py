from django.contrib import admin
from Course_App.models import *
# Register your models here.
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)