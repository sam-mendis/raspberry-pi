from random import randint
from random import seed
from datetime import datetime
# For the GUI
from tkinter import *
from multiprocessing import Process
# from temperature_sensor_code import *

# For the resetting
# for the time part
import time
# For DS18B20
import glob
import gpiozero
import os
import sys
import json
import array
import csv
from typing import AsyncContextManager

# need to have this before any tkinter program.
# this creates the window for the gui
# Temperature sesnor is goig to be connected to GPIO 4
root = Tk()

'''Sorting out date and time'''
date_time = datetime.now()
Date = '%s/%s/%s' % (date_time.day, date_time.month, date_time.year)
Time = '%s:%s:%s' % (date_time.hour, date_time.minute, date_time.second)

# Something needed for Temperature Sensor
'''
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
'''


class parameters:

    def __init__(self, name):
        self.name = name
        self.value = float
        self.actual = float
        self.desired = float

    def values(self, value):
        self.value = value

    def actualv(self, actual):
        self.actual = actual

    def desiredv(self, desired):
        self.desired = desired


# Assuming only working with 2 gases
A = parameters("Atmospheric Temperature")

'''A.values(25)
A.actualv(35)
A.desiredv(40)'''

T = parameters("Desired Temperature")
t = parameters('time in seconds')
g = parameters("Gas 1 Percentage")
V = parameters("Voltage to hold cells at")
t.desiredv(10)
'''print(A.value)
print(A.actual)
print(A.desired)'''

# fake read temp


def read_temp():
    return 100


def desired_temp():
    return 120

# The Temperature controller which will run inside the function control


def temp_control(Temp):
    Temp.actualv(read_temp())
    Temp.desiredv(desired_temp())

    if Temp.actual < Temp.desired:
        "switch on Heater by closing SSR"
        # Switching GPIO 6 on
    else:
        '''switch off heater'''
        # Switching GPIO 6 off
    return Temp.actual

# Building the Controller that will run the entire system. The inputs are the classes Temp,time,gas and voltage.


def control(Temp, Time, Gas, Voltage):
    t0 = time.time()
    time.sleep(1)
    Time.actualv(round((time.time()-t0), 2))
    Temperature = [Time.actual, temp_control(Temp)]
    print(Temperature)
    end = Time.desired + t0


control(T, t, g, V)

# def controller1(fuck):
# fuck.values(35)
# print(fuck.value)
# controller1(A)
""""
root.title("Environmental Controller for Testing Container")


frame_s = Frame(root)
frame_s.grid()

inputlabel = Label(frame_s, text="Manual Input", font=" Times 16", width=75)
inputlabel.grid(row=0, column=0, columnspan=6)
atmlabel = Label(
    frame_s, text="Atmospheric Temp/\N{DEGREE SIGN}C", font=" Times 13", width=15)
atmlabel.grid(row=2, column=0)
templabel = Label(
    frame_s, text="Temp/\N{DEGREE SIGN}C", font=" Times 13", width=15)
templabel.grid(row=2, column=1)


root.mainloop()
"""
