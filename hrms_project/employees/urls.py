from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/<int:emp_id>/", views.employee_detail, name="employee_detail"),
    path("api/attendance/", views.mark_attendance, name="mark_attendance"),
    path("report/", views.department_report, name="department_report"),  # ✅ ADD THIS
]
