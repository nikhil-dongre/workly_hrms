
from django.contrib import admin
from django.urls import path,include
from .views import PunchInView
urlpatterns = [
    path('punch_in/',PunchInView.as_view()),
   
]
