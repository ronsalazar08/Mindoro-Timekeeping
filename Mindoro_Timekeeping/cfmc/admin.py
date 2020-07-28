from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from django.http import HttpResponse
from django.urls import path

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(employee)
class emp(admin.ModelAdmin):
    fields = ['thumbnail', 'picture', 't1', 't2', 't3', 't4', 't5', 'user_id',
              'firstname', 'middlename', 'lastname', 'birthday', 'status']
    readonly_fields = ['thumbnail']
    list_display = ['__str__', 't1', 't2',
                    't3', 't4', 't5', 'status', 'action']
    list_filter = ['status']
    search_fields = ['firstname', 'lastname']
    ordering = (['lastname'])
    # change_list_template = 'admin/cfmc/employee_change_list.html'
    change_form_template = 'admin/cfmc/employee_change_form.html'


@admin.register(logbox)
class logboxAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date_time', 'transaction']
    list_filter = ['transaction']
    search_fields = ['date_time']
