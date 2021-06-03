from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.apps import apps
from datetime import datetime
import json
from .models import *
import os
import signal
import serial
import time
import subprocess as sp



@login_required(login_url='/admin') 
def record_per_employee(request, tid):
    emp = employee.objects.get(id=tid)
    record = logbox.objects.raw(
        f'''
        SELECT
            DISTINCT DATE(date_time) as petsa, 1 as id,
            TIME_FORMAT((SELECT TIME(date_time) FROM cfmc_logbox WHERE employee_id = '{tid}' AND transaction = 'I' AND DATE(date_time) = petsa), '%%h:%%i %%p') AS timeIn,
            TIME_FORMAT((SELECT TIME(date_time) FROM cfmc_logbox WHERE employee_id = '{tid}' AND transaction = 'O' AND DATE(date_time) = petsa), '%%h:%%i %%p') AS timeOut
        FROM cfmc_logbox AS SOD WHERE employee_id = '{tid}' ORDER BY petsa;
        '''
    )
    context = {
        'emp': emp,
        'record': record,
        
    }
    return render(request, 'cfmc/record.html', context)

def index(request):
    if request.method == "POST":
        tid = request.POST.get('inputBox')
        return redirect(f'../display/{tid}')
    return render(request, 'cfmc/index.html')

def display(request, tid):
    transaction = 'ERROR'
    color = 'indianred'
    emp = employee.objects.raw(f'''SELECT * FROM cfmc_employee WHERE 
                                t1='{tid}' or t2='{tid}' or t3='{tid}' or t4='{tid}' or t5='{tid}';''' )
    try:
        if len(emp) != 0:
            tid = emp[0].t1
            rec = logbox.objects.filter(employee=tid).filter(date_time__startswith=timezone.now().date())
            if rec.count() != 0:            #if has login today
                timestamp = rec.filter(transaction="I")[0].date_time + timezone.timedelta(minutes=30)
                if timezone.now() < timestamp:
                    transaction = 'REPEATED LOGIN'
                    color = 'indianred'
                else:
                    if rec.filter(transaction="O").count() != 0:
                        transaction = 'REPEATED LOGOUT'
                        color = 'indianred'
                    else:
                        query = logbox(date_time=timezone.now(), transaction='O', employee = emp[0])
                        query.save()
                        transaction = 'LOGOUT'
                        color = 'mediumseagreen'
                    
            else:                            #login
                query = logbox(date_time=timezone.now(), transaction='I', employee = emp[0])
                query.save()
                transaction = 'LOGIN'
                color = 'mediumseagreen'

            context = {
                        'color'    : color,
                        'transaction' : transaction,
                        'emp': emp,
                        'orasan': timezone.now().strftime('%I:%M %p')
                    }
    except:
        context = {
                    'color'    : color,
                    'transaction' : transaction,
                    'emp': emp,
                    'orasan': "PLEASE REPORT TO ADMIN"
                }
    return render(request, 'cfmc/display.html', context)


def setT1(request, t):
    emp = employee.objects.raw(f'''
                                SELECT * FROM cfmc_employee WHERE
                                t1 = {t} or
                                t2 = {t} or
                                t3 = {t} or
                                t4 = {t} or
                                t5 = {t}
                                ''')
    ser = serial.Serial('/dev/ttyUSB0',9600)
    f = open("/home/pi/Desktop/pid.txt", "r")
    pid1 = int(f.read())
    proctest = sp.Popen(['python3', '/home/pi/Desktop/TYPE/testbox.py'])
    time.sleep(3)
    # os.kill(pid1, signal.SIGKILL)
    ser.write(str.encode('1'))
    # proctest = sp.Popen(['mousepad','/home/pi/Desktop/test.txt'])
    pidtest = proctest.pid
    time.sleep(1)
    ser.write(str.encode(str(t)))
    
    context= {
        'emp' : emp[0]
    }
    return render(request, 'cfmc/set.html', context)