from django.shortcuts import render, redirect
from cfmc.models import *
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
import json
from django.db import connection
from django.utils import timezone
from django.conf import settings


@login_required
def CurrentWeek(request):
    t = timezone.now().weekday()
    ts = timezone.now() + timezone.timedelta(days=-t)
    ts = ts + timezone.timedelta(days=-1)

    petsa = []
    petsa1 = []
    for c in range(7):
        pet = ts + timezone.timedelta(days=c)
        petsa.append(str(pet.date()))
        petsa1.append(pet.date())

    dictOfWords = {i: petsa1[i] for i in range(0, len(petsa1))}
    query = employee.objects.raw(
        '''SELECT DISTINCT employee_id as id,
 
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id) AS ti1,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id) AS to1,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id) AS ti2,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id) AS to2,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id) AS ti3,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id) AS to3,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id) AS ti4,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id) AS to4,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id) AS ti5,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id) AS to5,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id) AS ti6,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id) AS to6,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id) AS ti7,
        (SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id) AS to7,
        (SELECT CONCAT(lastname, ', ', firstname, ' ', LEFT(middlename , 10)) AS name FROM cfmc_employee WHERE cfmc_employee.id = olo.employee_id) AS name
        FROM cfmc_logbox AS olo ORDER BY name;'''
    )

    query1 = logbox.objects.raw('''select employee_id as id,

        (select user_id from cfmc_employee where cfmc_employee.id = cfmc_logbox.employee_id ) as userID,
        date_format(date_time, "%%Y%%m%%d") as DateLog,
        time_format(date_time, "%%H%%i") as TimeLog,
        transaction as event from cfmc_logbox where date(date_time) >= \'''' + petsa[0] + '''\' and date(date_time) <= \'''' + petsa[6] + '''\' ;'''
                                )

    context = {
        'query': query,
        'query1': query1,
        'ts': dictOfWords
    }
    return render(request, 'schedule/week.html', context)


@login_required
def LastWeek(request):
    t = timezone.now().weekday()
    ts = timezone.now() + timezone.timedelta(days=-t)
    ts = ts + timezone.timedelta(days=-8)

    petsa = []
    petsa1 = []
    for c in range(7):
        pet = ts + timezone.timedelta(days=c)
        petsa.append(str(pet.date()))
        petsa1.append(pet.date())

    dictOfWords = {i: petsa1[i] for i in range(0, len(petsa1))}
    query = employee.objects.raw(
        '''SELECT DISTINCT employee_id as id,
 
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti1,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to1,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti2,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to2,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti3,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to3,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti4,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to4,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti5,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to5,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti6,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to6,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti7,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to7,
        (SELECT CONCAT(lastname, ', ', firstname, ' ', LEFT(middlename , 10)) AS name FROM cfmc_employee WHERE cfmc_employee.id = olo.employee_id) AS name
        FROM cfmc_logbox AS olo ORDER BY name;'''
    )

    query1 = logbox.objects.raw('''select employee_id as id,

        (select user_id from cfmc_employee where cfmc_employee.id = cfmc_logbox.employee_id ) as userID,
        date_format(date_time, "%%Y%%m%%d") as DateLog,
        time_format(date_time, "%%H%%i") as TimeLog,
        transaction as event from cfmc_logbox where date(date_time) >= \'''' + petsa[0] + '''\' and date(date_time) <= \'''' + petsa[6] + '''\' ;'''
                                )

    context = {
        'query': query,
        'query1': query1,
        'ts': dictOfWords
    }
    return render(request, 'schedule/week.html', context)


@login_required
def Last2Week(request):
    t = timezone.now().weekday()
    ts = timezone.now() + timezone.timedelta(days=-t)
    ts = ts + timezone.timedelta(days=-15)

    petsa = []
    petsa1 = []
    for c in range(7):
        pet = ts + timezone.timedelta(days=c)
        petsa.append(str(pet.date()))
        petsa1.append(pet.date())

    dictOfWords = {i: petsa1[i] for i in range(0, len(petsa1))}
    query = employee.objects.raw(
        '''SELECT DISTINCT employee_id as id,
 
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti1,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to1,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti2,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to2,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti3,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to3,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti4,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to4,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti5,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to5,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti6,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to6,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti7,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to7,
        (SELECT CONCAT(lastname, ', ', firstname, ' ', LEFT(middlename , 10)) AS name FROM cfmc_employee WHERE cfmc_employee.id = olo.employee_id) AS name
        FROM cfmc_logbox AS olo ORDER BY name;'''
    )

    query1 = logbox.objects.raw('''select employee_id as id,

        (select user_id from cfmc_employee where cfmc_employee.id = cfmc_logbox.employee_id ) as userID,
        date_format(date_time, "%%Y%%m%%d") as DateLog,
        time_format(date_time, "%%H%%i") as TimeLog,
        transaction as event from cfmc_logbox where date(date_time) >= \'''' + petsa[0] + '''\' and date(date_time) <= \'''' + petsa[6] + '''\' ;'''
                                )

    context = {
        'query': query,
        'query1': query1,
        'ts': dictOfWords
    }
    return render(request, 'schedule/week.html', context)


@login_required
def Last3Week(request):
    t = timezone.now().weekday()
    ts = timezone.now() + timezone.timedelta(days=-t)
    ts = ts + timezone.timedelta(days=-22)

    petsa = []
    petsa1 = []
    for c in range(7):
        pet = ts + timezone.timedelta(days=c)
        petsa.append(str(pet.date()))
        petsa1.append(pet.date())

    dictOfWords = {i: petsa1[i] for i in range(0, len(petsa1))}
    query = employee.objects.raw(
        '''SELECT DISTINCT employee_id as id,
 
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti1,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[0] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to1,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti2,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[1] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to2,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti3,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[2] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to3,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti4,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[3] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to4,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti5,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[4] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to5,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti6,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[5] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to6,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'I' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS ti7,
        TIME_FORMAT((SELECT date_time FROM cfmc_logbox WHERE DATE(date_time) = \'''' + petsa[6] + '''\' AND transaction = 'O' AND employee_id = olo.employee_id), '%%h:%%i %%p') AS to7,
        (SELECT CONCAT(lastname, ', ', firstname, ' ', LEFT(middlename , 10)) AS name FROM cfmc_employee WHERE cfmc_employee.id = olo.employee_id) AS name
        FROM cfmc_logbox AS olo ORDER BY name;'''
    )

    query1 = logbox.objects.raw('''select employee_id as id,

        (select user_id from cfmc_employee where cfmc_employee.id = cfmc_logbox.employee_id ) as userID,
        date_format(date_time, "%%Y%%m%%d") as DateLog,
        time_format(date_time, "%%H%%i") as TimeLog,
        transaction as event from cfmc_logbox where date(date_time) >= \'''' + petsa[0] + '''\' and date(date_time) <= \'''' + petsa[6] + '''\' ;'''
                                )

    context = {
        'query': query,
        'query1': query1,
        'ts': dictOfWords
    }
    return render(request, 'schedule/week.html', context)


def validation_view(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "/validation")
    # print(img_list)
    context = {"images": img_list}
    return render (request, 'schedule/validation_images.html', context)


def validation_clear(request):
    os.system("rm -f /home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/validation/*")
    messages.success(request, f' The validations was cleared successfully. ')
    return redirect('admin:index')


def device_restart(request):
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    # subprocess.call("/home/pi/Desktop/restart.sh")
    return redirect('admin:index')
    

def device_shutdown(request):
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    # subprocess.call("/home/pi/Desktop/restart.sh")
    return redirect('admin:index')