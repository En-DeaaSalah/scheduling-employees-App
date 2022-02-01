from urllib import response
from rest_framework.views import APIView

from rest_framework.response import Response

from .models import *

from .serializers import *


class EmployeeApi(APIView):

    def get(self, request):

        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
