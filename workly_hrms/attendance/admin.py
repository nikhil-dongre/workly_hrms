from django.contrib import admin
from .models import Attendance,AttendanceLog
# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display=['date','employee__emp_code']

class AttendanceLogAdmin(admin.ModelAdmin):
    list_display=['punch_in','punch_out']


admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(AttendanceLog,AttendanceLogAdmin)