
from django.contrib import admin
from django.urls import path,include
from .views import UserRegister,LoginView
urlpatterns = [
    path('register/',UserRegister.as_view(),name='register_view'),
    path('login/',LoginView.as_view(),name='login_view'),
]
