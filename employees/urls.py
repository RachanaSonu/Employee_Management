from django.urls import path
from .views import employee_list, add_employee, direct_add_employee, department_list, add_department

urlpatterns = [
    path('department/<int:department_id>/', employee_list, name='employee_list'),
    path('department/<int:department_id>/add_employee/', add_employee, name='add_employee'),
    path('add_employee/', direct_add_employee, name='direct_add_employee'),
    path('department/', department_list, name='department_list'),
    path('add_department/', add_department, name='add_department'),
]
