
from django.contrib import admin
from django.urls import path,include
from .views import PunchInView,PunchOutView
urlpatterns = [
    path('punch_in/',PunchInView.as_view()),
    path('punch_out/',PunchOutView.as_view()),
   
]
