from django.db import models

class Employee(models.Model):
    """
    Model to store employee details
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    """
    Model to store employee attendance
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField()

    def __str__(self):
        return f"{self.employee.name} - {self.date}"