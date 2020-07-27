from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
from . import views
from django.http import HttpResponse
from django.urls import path
from django.utils import timezone

global current_week, last_week, last2_week, last3_week
t = timezone.now().weekday()
ts = timezone.now() + timezone.timedelta(days=-t)
currentweekf = ts + timezone.timedelta(days=-1)
currentweekl = ts + timezone.timedelta(days=+5)
last3weekf = ts + timezone.timedelta(days=-22)
last3weekl = ts + timezone.timedelta(days=-16)
last2weekf = ts + timezone.timedelta(days=-15)
last2weekl = ts + timezone.timedelta(days=-9)
lastweekf = ts + timezone.timedelta(days=-8)
lastweekl = ts + timezone.timedelta(days=-2)


current_week = currentweekf.strftime(
    "%B %d, %Y") + ' - ' + currentweekl.strftime("%B %d %Y")
last_week = lastweekf.strftime("%B %d, %Y") + \
    ' - ' + lastweekl.strftime("%B %d %Y")
last2_week = last2weekf.strftime(
    "%B %d, %Y") + ' - ' + last2weekl.strftime("%B %d %Y")
last3_week = last3weekf.strftime(
    "%B %d, %Y") + ' - ' + last3weekl.strftime("%B %d %Y")
# my dummy model # ====================================================


class CurWeek(models.Model):
    class Meta:
        verbose_name_plural = str('1. ' + current_week)
        app_label = 'schedule'


class LasWeek(models.Model):
    class Meta:
        verbose_name_plural = str('2.  ' + last_week)
        app_label = 'schedule'


class Las2Week(models.Model):
    class Meta:
        verbose_name_plural = str('3. ' + last2_week)
        app_label = 'schedule'


class Las3Week(models.Model):
    class Meta:
        verbose_name_plural = str('4. ' + last3_week)
        app_label = 'schedule'


class CurWeekModelAdmin(admin.ModelAdmin):
    model = CurWeek

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', views.CurrentWeek, name=view_name),
        ]


class LasWeekModelAdmin(admin.ModelAdmin):
    model = LasWeek

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', views.LastWeek, name=view_name),
        ]


class Las2WeekModelAdmin(admin.ModelAdmin):
    model = Las2Week

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', views.Last2Week, name=view_name),
        ]


class Las3WeekModelAdmin(admin.ModelAdmin):
    model = Las3Week

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', views.Last3Week, name=view_name),
        ]


admin.site.register(CurWeek, CurWeekModelAdmin)
admin.site.register(LasWeek, LasWeekModelAdmin)
admin.site.register(Las2Week, Las2WeekModelAdmin)
admin.site.register(Las3Week, Las3WeekModelAdmin)
