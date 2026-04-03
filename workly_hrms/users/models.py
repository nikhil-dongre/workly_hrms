from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("The user must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('role',User.Role.ADMIN)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("User should be a staff ")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("User should be a super user ")
        super_user=self.create_user(email,password,**extra_fields)


        return super_user
        

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        HR = 'HR', 'HR'
        MANAGER = 'MANAGER', 'Manager'
        EMPLOYEE = 'EMPLOYEE', 'Employee'
    role = models.CharField(max_length=20,choices=Role.choices,default=Role.EMPLOYEE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='profile_photos/',null=True, blank=True,)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = None
    def __str__(self):
        return self.email
    
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    @property
    def is_hr(self):
        return self.role == self.Role.HR
    
    @property
    def is_employee(self):
        return self.role == self.Role.EMPLOYEE
    
    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER
    
    objects = UserManager()