from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from organization.models import Department,Designation
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    emp_code = models.CharField(unique=True,null=False,blank=False,max_length=6)
    joining_date = models.DateField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    salary = models.DecimalField(decimal_places=4,max_digits=10)
    manager = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,related_name='subordinates')
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True,null=True)
    emergency_contact = models.CharField(max_length=15)
    place_of_birth = models.CharField(max_length=20,blank=True,null=True)


    def __str__(self):
        return self.emp_code