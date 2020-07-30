#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import serial
import subprocess as sp
from pynput.keyboard import Key, Controller
keyboard = Controller()

ser = serial.Serial('/dev/ttyUSB0',9600)

def openType():
    #os.system('python seria_test.py')
    ser.write(str.encode('2'))
    proc = sp.Popen(['python3','/home/pi/Desktop/TYPE/seria_test.py'])
    global pid1
    pid1 = proc.pid
    return pid1

pid1 = openType()
f = open("pid.txt", "w")
f.write(str(pid1))
f.close()


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mindoro_Timekeeping.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()