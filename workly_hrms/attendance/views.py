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