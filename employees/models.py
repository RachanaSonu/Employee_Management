from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
