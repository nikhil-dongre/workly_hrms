from django.db import models
from employees.models import Employee
# Create your models here.
from datetime import timedelta

class Attendance(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True
    )
    total_worked_hours = models.DurationField(default=timedelta(0))
    def __str__(self):
        return self.employee.emp_code if self.employee else "No Employee"
    class Meta:
        unique_together = ('employee', 'date','total_worked_hours')


class AttendanceLog(models.Model):
    punch_in = models.DateTimeField()
    punch_out = models.DateTimeField(blank=True,null=True)
    attendance = models.ForeignKey(Attendance,on_delete=models.CASCADE,related_name='logs')

    def __str__(self):
        return f"{self.attendance.employee.emp_code} - {self.punch_in}"