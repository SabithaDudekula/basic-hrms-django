from django.contrib import admin
from .models import Employee, Attendance

# Register Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "department", "designation", "email")


# Register Attendance model
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "in_time", "out_time")
