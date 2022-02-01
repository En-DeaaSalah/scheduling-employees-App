
from unicodedata import name
from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

    # path('employees/', EmployeeApi.as_view())


    path('employees/', views.employeesList, name='employeesList'),

    path('employees/<str:pk>', views.employee, name='one_employee'),

    path('jobs/', views.positionList, name='positionsList'),

    path('jobs/<str:pk>', views.position, name='one_position'),






]

urlpatterns = format_suffix_patterns(urlpatterns)
