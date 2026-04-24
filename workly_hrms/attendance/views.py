from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from employees.models import Employee
from .models import Attendance, AttendanceLog

from .serializers import AttendanceSerializer
class PunchInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        current_user = request.user
        time = timezone.now()
        today = time.date()

        # 🔹 Get employee safely
        try:
            emp_rec = Employee.objects.get(user=current_user)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        # 🔹 Get or create attendance
        attendance_obj, created = Attendance.objects.get_or_create(
            employee=emp_rec,
            date=today
        )

        # 🔹 Check open session
        open_log = AttendanceLog.objects.filter(
            attendance=attendance_obj,
            punch_out__isnull=True
        ).first()

        if open_log:
            return Response({"message": "Already punched in"})

        # 🔹 Create new punch-in log
        AttendanceLog.objects.create(
            attendance=attendance_obj,
            punch_in=time
        )
        return Response({"message": "Punched in successfully"})
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from employees.models import Employee
from .models import Attendance, AttendanceLog


class PunchOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        current_user = request.user
        now = timezone.now()
        today = now.date()

        # 🔹 Get employee
        try:
            emp_rec = Employee.objects.get(user=current_user)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        # 🔹 Get today's attendance
        try:
            attendance_obj = Attendance.objects.get(employee=emp_rec, date=today)
        except Attendance.DoesNotExist:
            return Response({"error": "No attendance record for today"}, status=404)

        # 🔹 Get open punch-in session
        punch_in_log = AttendanceLog.objects.filter(
            attendance=attendance_obj,
            punch_out__isnull=True
        ).first()

        if not punch_in_log:
            return Response(
                {"error": "No open punch-in session. Please punch in first."},
                status=400
            )

        # 🔹 Calculate duration BEFORE updating punch_out
        duration = now - punch_in_log.punch_in

        # 🔹 Update attendance total (no if/else needed)
        attendance_obj.total_worked_hours += duration

        # 🔹 Close session
        punch_in_log.punch_out = now

        # 🔹 Save both
        punch_in_log.save()
        attendance_obj.save()

        return Response(
            {"message": "Punch out was successful"},
            status=200
        )
    
class TodayAttendance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        current_user = request.user
        now = timezone.now()
        date = now.date()
        try:
            emp_rec = Employee.objects.get(user = current_user)
        except Employee.DoesNotExist:
            return Response({"error": "Employee does not exist"}, status=404)
        
        try:
            attendance_rec = Attendance.objects.get(employee = emp_rec,date=date)
        except Attendance.DoesNotExist:
            return Response({"error": "Attendance for today is not available"}, status=404)
        status = ''
        if attendance_rec:
            open_atten_log = AttendanceLog.objects.filter(attendance = attendance_rec,
                                                          punch_out__isnull=True , punch_in__isnull=False).exists()
            
            if open_atten_log:
                status = 'IN'
            else:
                status = 'OUT'
        serializer = AttendanceSerializer(attendance_rec)

        return Response({
            "status": status,
            "data": serializer.data
        })
