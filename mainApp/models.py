from turtle import position
from typing import Text
from django.db import models


class Job(models.Model):

    position_name = models.TextField()


class Employee(models.Model):

    first_name = models.CharField(max_length=30)

    second_name = models.CharField(max_length=30)

    email = models.EmailField(max_length=20, null=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):

        return self.first_name


# each employee has Profile

class EmployeeProfile(models.Model):

    # The relationship between employee called "User" and  Profile is one-to-one
    owner = models.OneToOneField(
        Employee, on_delete=models.CASCADE)

    birth_date = models.DateField(null=True, blank=True)

    img = models.ImageField(null=True)

    country = models.TextField(null=True)


class schedule(models.Model):

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee')

    position = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='position')

    date = models.DateField(null=True, blank=True)

    startTime = models.TimeField(auto_now=False, auto_now_add=False)

    endTime = models.TimeField(auto_now=False, auto_now_add=False)

    breakTime = models.IntegerField()  # 20 min example
