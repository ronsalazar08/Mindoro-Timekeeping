from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from django.http import HttpResponse
from django.urls import path

# admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(employee)
class emp(admin.ModelAdmin):
    # fields = ['thumbnail', 'picture', 'user_id',
            #   'firstname', 'middlename', 'lastname', 'birthday',]
            #   't1', 't2', 't3', 't4', 't5', 'status']
    # readonly_fields = ['thumbnail']
    
    fields = ['picture1', 'picture2', 'picture3', 'picture4', 'picture5', 'user_id',
    # fields = ['picture1', 'user_id',
              'firstname', 'middlename', 'lastname', 'birthday',]
    list_display = ['__str__', 'user_id', 'action']
    # list_filter = ['status']
    search_fields = ['firstname', 'lastname']
    ordering = (['lastname'])
    actions = None
    # change_list_template = 'admin/cfmc/employee_change_list.html'
    change_form_template = 'admin/cfmc/employee_change_form.html'


@admin.register(logbox)
class logboxAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date_time', 'transaction']
    list_filter = ['transaction']
    search_fields = ['employee__lastname', 'employee__firstname', 'date_time']
