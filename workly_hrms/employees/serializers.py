from rest_framework import serializers
from .models import Employee
class EmpSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name',readonly=True)
    email = serializers.CharField(source='user.email',readonly=True)
    class Meta:
        model = Employee
        fields = ['emp_code','joining_date','department','designation',
                  'salary','manager','phone','user_name','email']

