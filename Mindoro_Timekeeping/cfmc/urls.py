from django.urls import path, include
from . import views

urlpatterns = [
    path('record/<int:tid>', views.record_per_employee, name='record'),
    path('index/', views.index, name='index'),
    path('display/<slug:tid>', views.display, name='display'),
    path('setT1/<int:t>', views.setT1, name='setT1'),
]