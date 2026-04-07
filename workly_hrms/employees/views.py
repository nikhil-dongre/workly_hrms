from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmpSerializer,PersonalSerializer,ContactSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Employee,Department,Designation
# Create your views here.

class EmpView(APIView):

    def get(self,request):
        current_user = request.user
        try:
            emp_rec = Employee.objects.get(user =current_user)
            serializer = EmpSerializer(emp_rec)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({"error":'employee does not exists'})
        


class PersonalView(APIView):
    def get(self,request):
        current_user = request.user
        try:
            emp_rec = Employee.objects.get(user =current_user)
            serializer = PersonalSerializer(emp_rec)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({"error":'employee does not exists'})
        

class ContactView(APIView):
    def get(self,request):
        current_user = request.user
        try:
            emp_rec = Employee.objects.get(user =current_user)
            serializer = ContactSerializer(emp_rec)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({"error":'employee does not exists'})
        

