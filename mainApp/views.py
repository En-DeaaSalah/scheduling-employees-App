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
def get_Positions_Assiment(request):

    positionsAssiment = schedule.objects.all()
    serializer = positionAssimentSerializer(positionsAssiment, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_employees_List(request):

    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_position_List(request):

    positions = Job.objects.all()
    serializer = JobSerializer(positions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_employee(request, pk):

    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_position(request, pk):

    positions = Job.objects.get(id=pk)
    serializer = JobSerializer(positions, many=False)
    return Response(serializer.data)


# give job id and return schedule details for this position (job)

@api_view(['GET'])
def get_emp_of_position(request, pk):

    assiment = schedule.objects.get(position=pk)
    serializer = positionAssimentSerializer(assiment, many=False)
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


@api_view(['POST'])
def positionAssiment(request):
    assiment = positionAssimentSerializer(data=request.data)

    if assiment.is_valid():
        assiment.save()
    return Response(assiment.data)
