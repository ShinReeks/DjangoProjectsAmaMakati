from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ('name', 'course', 'gpa', 'is_active')
    list_filter   = ('course', 'is_active')
    search_fields = ('name', 'email')
