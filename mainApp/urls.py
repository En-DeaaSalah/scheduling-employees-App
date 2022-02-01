from django.urls import path
from .views import *

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

    path('employees/', EmployeeApi.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
