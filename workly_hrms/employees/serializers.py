from rest_framework import serializers
from .models import Employee
class EmpSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name',read_only=True)
    email = serializers.CharField(source='user.email',read_only=True)
    class Meta:
        model = Employee
        fields = ['emp_code','joining_date','department','designation',
                  'salary','manager','phone','user_name','email']



class PersonalSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name',read_only=True)
    last_name = serializers.CharField(source='user.last_name',read_only=True)
    class Meta:
        model=Employee
        fields =['first_name','last_name','phone','address','emergency_contact','place_of_birth']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields =['phone','address','emergency_contact','place_of_birth']