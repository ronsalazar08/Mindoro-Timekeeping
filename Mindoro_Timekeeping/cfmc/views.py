from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
from datetime import datetime
import json
from .models import *

@login_required(login_url='/admin') 
def record_per_employee(request, tid):
    emp = employee.objects.get(id=tid)
    record = logbox.objects.raw(
        f'''
        SELECT
            DISTINCT DATE(date_time) as petsa, 1 as id,
            TIME_FORMAT((SELECT TIME(date_time) FROM cfmc_logbox WHERE t1 = '{emp.t1}' AND transaction = 'I' AND DATE(date_time) = petsa), '%%h:%%i %%p') AS timeIn,
            TIME_FORMAT((SELECT TIME(date_time) FROM cfmc_logbox WHERE t1 = '{emp.t1}' AND transaction = 'O' AND DATE(date_time) = petsa), '%%h:%%i %%p') AS timeOut
        FROM cfmc_logbox AS SOD WHERE t1 = '{emp.t1}' ORDER BY petsa;
        '''
    )
    context = {
        'emp': emp,
        'record': record,
        
    }
    return render(request, 'cfmc/record.html', context)