from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
import json

from .models import Employee, Attendance


def employee_list(request):
    """
    Display list of all employees
    """
    employees = Employee.objects.all()
    return render(
        request,
        "employees/employee_list.html",
        {"employees": employees}
    )


def employee_detail(request, emp_id):
    """
    Display employee details along with attendance
    """
    employee = get_object_or_404(Employee, id=emp_id)
    attendance = Attendance.objects.filter(employee=employee)

    return render(
        request,
        "employees/employee_detail.html",
        {
            "employee": employee,
            "attendance": attendance
        }
    )


@csrf_exempt
def mark_attendance(request):
    """
    API to mark attendance for an employee
    """
    if request.method == "POST":
        data = json.loads(request.body)

        employee = Employee.objects.get(id=data["employee_id"])

        Attendance.objects.create(
            employee=employee,
            date=data["date"],
            in_time=data["in_time"],
            out_time=data["out_time"]
        )

        return JsonResponse(
            {"message": "Attendance marked successfully"}
        )

    return JsonResponse(
        {"error": "Invalid request method"},
        status=400
    )


def department_report(request):
    """
    Display department-wise employee count
    """
    report = Employee.objects.values("department").annotate(
        count=Count("id")
    )

    return render(
        request,
        "employees/department_report.html",
        {"report": report}
    )
