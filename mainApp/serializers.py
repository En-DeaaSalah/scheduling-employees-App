from dataclasses import field
from importlib.metadata import files
from pyexpat import model
from statistics import mode
from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employee
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):

    class Meta:

        model = Job
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = EmployeeProfile
        fields = '__all__'
