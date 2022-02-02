
from unicodedata import name
from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

    # path('employees/', EmployeeApi.as_view())


    path('employees/', views.get_employees_List, name='employeesList'),


    path('employees/<int:pk>/', views.get_employee, name='one_employee'),


    path('jobs/', views.get_position_List, name='positionsList'),


    path('jobs/<int:pk>/', views.get_position, name='one_position'),


    path('jobs/add/', views.addPosition, name='add_position'),


    path('employees/add/', views.addEmployee, name='add_employee'),


    path('schedule/', views.get_Positions_Assiment, name='get_all_jobs_assiment'),

    path('assiment/', views.positionAssiment, name='get_all_jobs_assiment'),


    path('assiment/<int:pk>', views.get_emp_of_position,
         name='job_assiment_details'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
