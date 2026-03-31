from django.contrib import admin
from .models import Department,Designation
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','description','head']
    ordering = ['-id']


class DesignationAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    ordering = ['-id']

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Designation, DesignationAdmin)