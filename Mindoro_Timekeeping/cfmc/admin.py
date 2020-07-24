from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from django.http import HttpResponse
from django.urls import path

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(employee)
class emp(admin.ModelAdmin):
    fields = [
        # 'thumbnail',
        'picture',
        't1',
        't2',
        't3',
        't4',
        't5',
        'user_id',
        'firstname',
        'middlename',
        'lastname',
        'birthday',
        'status',] 
    readonly_fields = ['thumbnail']
    list_display = [
        '__str__',
        't1',
        't2',
        't3',
        't4',
        't5',
        'status',
    ]
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
    




# # my dummy model # ====================================================
# class DummyModel(models.Model):

#     class Meta:
#         verbose_name_plural = 'Dummy Model'
#         app_label = 'cfmc'

# def my_custom_view(request):
#     return HttpResponse('Admin Custom View')

# class DummyModelAdmin(admin.ModelAdmin):
#     model = DummyModel

#     def get_urls(self):
#         view_name = '{}_{}_changelist'.format(
#             self.model._meta.app_label, self.model._meta.model_name)
#         return [
#             path('my_admin_path/', my_custom_view, name=view_name),
#         ]
# admin.site.register(DummyModel, DummyModelAdmin)