from .models import Attendance,AttendanceLog
from django.shortcuts import render
from django.http import HttpRequest 
from datetime import datetime
from django.utils import timezone
def check_open_session(attendance):

    check_punch_log = AttendanceLog.objects.filter(attendance = attendance,
                                                punch_out__isnull=True).exists()

    print(check_punch_log)


    return check_punch_log

def punch_in(employee):
    time = timezone.now()
    today = time.today()
    # print(time)
    # attendance_obj = Attendance.objects.filter(employee=employee,date =time,
    #                                            )
    attendance_obj,created = Attendance.objects.get_or_create(
        employee=employee,date =today,
    )

    if check_open_session(attendance_obj):
        return "already punched in"
    
    if attendance_obj:
        attendancelog_obj = AttendanceLog.objects.create(attendance=attendance_obj,
                                                         punch_in=time)
        return "Punch in successfull"
def punch_out(employee):
    now = timezone.now()
    today = now.date()

    # Get today's attendance
    attendance = Attendance.objects.filter(
        employee=employee,
        date=today
    ).first()

    if not attendance:
        return "No attendance found"

    # Get open session
    log = AttendanceLog.objects.filter(
        attendance=attendance,
        punch_out__isnull=True
    ).first()

    if not log:
        return "No active session to punch out"

    # Close session
    log.punch_out = now
    log.save()

    return "Punch out successful"