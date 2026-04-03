from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','role','is_staff']
    list_filter = ['role','is_staff']
    search_fields = ['email','first_name','last_name']
    ordering = ['-id']

    fieldsets = (
        ('Personal Data', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'profile_photo',
                       'password','last_login','date_joined')
        }),
        ('Permissions', {
            'fields': ('role', 'is_staff', 'is_superuser', 'is_active')
        }),
    )

    readonly_fields = ['last_login','date_joined']  

admin.site.register(User,UserAdmin)
