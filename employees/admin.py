from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_code','user','department','designation']
    ordering = ['-id']
    list_filter = ['department','designation']
    search_fields=['emp_code','user__email']

admin.site.register(Employee,EmployeeAdmin)



