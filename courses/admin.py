from django.contrib import admin
from .models import Course, Assessment

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title' , 'url', 'create', 'update', 'active')

@admin.register(Assessment)
class Assessment(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'assessment', 'create', 'update', 'active')