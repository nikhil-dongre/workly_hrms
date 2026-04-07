
from django.contrib import admin
from django.urls import path,include
from .views import EmpView,PersonalView,ContactView
urlpatterns = [
    # path('register/',UserRegister.as_view(),name='register_view'),
    path('me/',EmpView.as_view(),name='emp_view'),
    path('personal/',PersonalView.as_view(),name='personal_view'),
    path('contact/',ContactView.as_view(),name='contact_view')
]
