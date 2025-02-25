from django.contrib import admin
from django.urls import path, include
from .views import home_page, facultys, FacultyDetailView, schedule, GroupDetailView
from .models import Group


urlpatterns = [
    path('', home_page, name='home_page'),
    path('facultys', facultys, name='facultys'),
    path('facultys/<int:pk>', FacultyDetailView.as_view(), name='faculty-detail'),
    path('schedule', schedule, name='schedule'),
    path('schedule/<int:pk>', GroupDetailView.as_view(), name='schedule-detail'),
]
