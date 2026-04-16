from django.shortcuts import render
from rest_framework.views import APIView
from .models import Attendance,AttendanceLog
from employees.models import Employee
from datetime import date
from django.utils import timezone

# Create your views here.
class PunchInView(APIView):
    print("PUnchinview")
    def post(self,request):
        data = request.data
        current_user = request.user
        time = timezone.now()
        today = time.today()
        emp_rec = Employee.objects.get(user =current_user)
        attendance_obj = Attendance.objects.get_or_create(
            employee=current_user,
            date= today
        )
        # if attendance_obj.date == data.date:




