from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from employees.models import Employee
from .models import Attendance, AttendanceLog


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
    
    
class PunchOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        current_user = request.user
        time = timezone.now()
        today = time.date()
        
        try:
            emp_rec = Employee.objects.get(user=current_user)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        try:
            attendance_obj = Attendance.objects.get(employee=emp_rec, date=today)
        except Attendance.DoesNotExist:
            return Response({"error": "No attendance record for today"}, status=404)

        punch_in_log = AttendanceLog.objects.filter(
            attendance=attendance_obj,
            punch_out__isnull=True,
            punch_in__isnull=False
        ).first()
        
        if not punch_in_log:
            return Response(
                {"error": "No open punch-in session. Please punch in first."},
                status=400
            )

        punch_in_log.punch_out = time
        punch_in_log.save()
        return Response(
            {"success": "Punch out was successful"},
            status=200
        )