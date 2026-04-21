from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    total_worked_hours = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['id', 'date', 'employee', 'total_worked_hours']

    def get_total_worked_hours(self, obj):
        duration = obj.total_worked_hours

        if not duration:
            return "00:00"

        total_seconds = int(duration.total_seconds())

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        return f"{hours:02}:{minutes:02}"