from sys import api_version
from urllib import response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import *

from .serializers import *


# class EmployeeApi(APIView):

#     def get(self, request):

#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         pass


# class PositionApi(APIView):
#     pass


@api_view(['GET'])
def employeesList(request):

    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def positionList(request):

    positions = Job.objects.all()
    serializer = JobSerializer(positions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def employee(request, pk):

    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def position(request, pk):

    positions = Job.objects.get(id=pk)
    serializer = JobSerializer(positions, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addEmployee(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addPosition(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
