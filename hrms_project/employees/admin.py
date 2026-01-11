from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin configuration for Employee model
    """
    list_display = (
        'name',
        'email',
        'address',
        'department',
        'designation',
        'date_of_joining',
    )
