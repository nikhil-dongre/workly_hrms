
from django.contrib import admin
from django.urls import path,include
from .views import PunchInView,PunchOutView,TodayAttendance
urlpatterns = [
    path('punch_in/',PunchInView.as_view()),
    path('punch_out/',PunchOutView.as_view()),
    path('today/', TodayAttendance.as_view(), name='today_attendance'),

]
