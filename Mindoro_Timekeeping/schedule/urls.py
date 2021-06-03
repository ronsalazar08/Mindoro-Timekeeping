from django.urls import path, include
from . import views

urlpatterns = [
    # path('CurrentWeek/', views.CurrentWeek, name='CurrentWeek'),
    path('validation/', views.validation_view, name='validation_view'),
    path('validation_clear/', views.validation_clear, name='validation_clear'),
    path('device_restart/', views.device_restart, name='device_restart'),
    path('device_shutdown/', views.device_shutdown, name='device_shutdown'),
]
