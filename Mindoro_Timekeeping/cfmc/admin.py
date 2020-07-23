from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)

class emp(admin.ModelAdmin):
    fields = [
        'thumbnail',
        'picture',
        't1',
        'user_id',
        'firstname',
        'middlename',
        'lastname',
        'birthday',
        'status',] 
    readonly_fields = ['thumbnail']
    list_display = [
        '__str__',
        'birthday',
        'status',
        'picture',
    ]
    list_filter = ['status']
    search_fields = ['firstname', 'lastname']
    ordering = (['lastname'])
    
    # change_list_template = 'admin/contractor/contractor_change_list.html'
admin.site.register(employee, emp)