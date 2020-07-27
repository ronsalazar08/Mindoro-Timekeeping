from django.urls import path, include
from . import views

urlpatterns = [
    path('CurrentWeek/', views.CurrentWeek, name='CurrentWeek'),
]
