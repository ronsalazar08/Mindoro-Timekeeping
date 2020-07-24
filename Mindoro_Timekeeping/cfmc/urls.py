from django.urls import path, include
from . import views

urlpatterns = [
    path('record/<int:tid>', views.record_per_employee, name='record'),
]