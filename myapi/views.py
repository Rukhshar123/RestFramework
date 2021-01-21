from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializers
from  .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('fullname')
    serializer_class = EmployeeSerializers