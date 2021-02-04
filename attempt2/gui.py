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
Current_Time = '%s:%s:%s' % (
    date_time.hour, date_time.minute, date_time.second)

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


# The function to measure the voltage
def measure_volts():
    return 0.1


def set_volts(Input):
    'The function to set the keythlay voltages to what I want'
    print(Input)

# The Temperature controller which will run inside the function control


def temp_control(Temp):
    Temp.actualv(read_temp())
    Temp.desiredv(desired_temp())

    if Temp.actual < Temp.desired:
        "switch on Heater by closing SSR"
        print('heater on')
        # Switching GPIO 6 on
    else:
        '''switch off heater'''
        # Switching GPIO 6 off
    return Temp.actual

# Building the Controller that will run the entire system. The inputs are the classes Temp,time,gas and voltage.


def control():
    t0 = time.time()
    Tend = time.time()+t.desired
    Temperature = [[Date, Current_Time], [
        'Time in seconds/s', 'Temperature/deg C'], [0, 20]]
    Cells_V = [[Date, Current_Time], [
        'Time in seconds/s', 'Cell 1 Voltage/V', 'Cell 2 Voltage/V', 'Cell 3 Voltage/V', 'Cell 4 Voltage/V', 'Cell 5 Voltage/V', 'Cell 6 Voltage/V'], [0, 0, 0, 0, 0, 0, 0]]
    time.sleep(1)

    # This while loop is where all the control neeeds to be done, includig gas and voltage control
    while time.time() < Tend:
        current_time = (round((time.time()-t0), 2))
        Temperature.append([current_time, temp_control(T)])

        if (time.time()-t0) < ((Tend-t0)/5):
            time.sleep(0.1)
        else:
            time.sleep(1)

    file = open('Temperature_data.csv', 'a+', newline='')

    with file:
        write = csv.writer(file)
        write.writerows(Temperature)

    print(Temperature)
    end = t.desired + t0


# A fucntion to check the ultiprocessing module is working fine
def counter():
    t = 0
    while t < 5:
        print(t)
        t = t+1
        time.sleep(1)
    print('End counter')


# For multiprocessing to work, the functions I am calling can not have input arguments
if __name__ == '__main__':
    p1 = Process(target=control)
    p1.start()
    p2 = Process(target=counter)
    p2.start()
    p1.join()
    p2.join()


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
