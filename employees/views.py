from django.shortcuts import get_object_or_404, render, redirect
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'employees/department_list.html', {'departments': departments})

def direct_add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list', department_id=form.cleaned_data['department'].id)
    else:
        form = EmployeeForm()

    departments = Department.objects.all()  # Add this line to get the list of departments
    return render(request, 'employees/add_employee.html', {'form': form, 'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect to the department list page
    else:
        form = DepartmentForm()

    departments = Department.objects.all()
    return render(request, 'employees/department_list.html', {'departments': departments, 'form': form})

def employee_list(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    employees = Employee.objects.filter(department=department)
    return render(request, 'employees/employee_list.html', {'department': department, 'employees': employees})

def add_employee(request, department_id):
    department = get_object_or_404(Department, pk=department_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.department = department
            employee.save()
            return redirect('employee_list', department_id=department.id)
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form, 'department': department})

def direct_add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_list', department_id=employee.department.id)
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form, 'department': None})
