from django.db import models
# from users.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(null=True,blank=True)
    head = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name', 'department')