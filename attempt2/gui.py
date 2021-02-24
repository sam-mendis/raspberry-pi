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
import math  # for creating time varying voltage and temperature maps
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

T = parameters("Desired Temperature")
t = parameters('time in seconds')
g = parameters("Gas 1 Percentage")
V = parameters("Voltage to hold cells at")
M = parameters("Measurement Intervals")
I = parameters(
    "Time intervals where measurements are taking place defined by in hours")
I.desiredv([15, 30, 45, 60])
M.desiredv([0.5, 1, 5, 10])
t.desiredv(5)
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
        print('heater on(Switching GPIO 6 on)/or leaving on')
        # Switching GPIO 6 on
    else:
        '''switch off heater'''
        # Switching GPIO 6 off
    return Temp.actual

# Building the Controller that will run the entire system. The inputs are the classes Temp,time,gas and voltage.


def control_T():
    n = 0
    t0 = time.time()
    Tend1 = t0+I.desired[0]
    Tend2 = t0+I.desired[1]+I.desired[0]
    Tend3 = t0+I.desired[2] + I.desired[1]+I.desired[0]
    Tend4 = t0+I.desired[3]+I.desired[2] + I.desired[1]+I.desired[0]
    t1 = 0

    Temperature = [[Date, Current_Time], [
        'Time in seconds/s', 'Temperature/deg C'], [0, 20]]
    Cells_V = [[Date, Current_Time], [
        'Time in seconds/s', 'Cell 1 Voltage/V', 'Cell 2 Voltage/V', 'Cell 3 Voltage/V', 'Cell 4 Voltage/V', 'Cell 5 Voltage/V', 'Cell 6 Voltage/V'], [0, 0, 0, 0, 0, 0, 0]]

    # This while loop is where all the control neeeds to be done, includig gas and voltage control
    while time.time() < Tend1:

        current_time = (round((time.time()-t0), 2))
        Temperature.append([current_time, temp_control(T)])
        t1 = t1+1
        pause_time = (t1*(0.5)+t0)-time.time()
        time.sleep(pause_time)

    t1 = 0
    while Tend1 < time.time() < Tend2:
        print(time.time())
        current_time = (round((time.time()-t0), 2))
        Temperature.append([current_time, temp_control(T)])
        # This counter insures that the time is not getting out of sync in the different functions due to time taken for tasks to run
        t1 = t1+1
        pause_time = (t1*(1)+Tend1)-time.time()
        time.sleep(pause_time)

    t1 = 0
    while Tend2 < time.time() < Tend3:
        current_time = (round((time.time()-t0), 2))
        Temperature.append([current_time, temp_control(T)])
        t1 = t1+1
        pause_time = (t1*(5)+Tend2)-time.time()
        time.sleep(pause_time)
    t1 = 0

    while Tend3 < time.time() < Tend4:
        current_time = (round((time.time()-t0), 2))
        Temperature.append([current_time, temp_control(T)])
        t1 = t1+1
        pause_time = (t1*(10)+Tend3)-time.time()
        time.sleep(pause_time)

    file = open('Temperature_data.csv', 'a+', newline='')

    with file:
        write = csv.writer(file)
        write.writerows(Temperature)

    print(Temperature)
    end = t.desired + t0


# A fucntion to check the ultiprocessing module is working fine
def counter_V():
    t0 = time.time()
    t = 0
    while t < (I.desired[3]+I.desired[2] + I.desired[1]+I.desired[0]):
        print(t)
        t = t+1
        pause_time = (t+t0)-time.time()
        time.sleep(pause_time)


def read_volts():
    # Some function to measure the voltage of each cell
    t0 = time.time()

    V = [0, 0, 0, 0, 0, 0]
    V[0] = V[0]+1
    V[1] = V[1]+2
    V[2] = V[2]+3
    V[3] = V[3]+4
    V[4] = V[4]+5
    V[5] = V[5]+6
    return V


def control_tloop():
    t0 = time.time()


def Read_Values():
    t0 = time.time()

    # Writing Date and time of test to Voltage data file
    D_t = [[Date, Current_Time], [
        'Time in seconds/s', 'Temperature/deg C']]

    D_v = [[Date, Current_Time], [
        'Cell 1 Voltage', 'Cell 2 Voltage', 'Cell 3 Voltage', 'Cell 4 Voltage', 'Cell 5 Voltage', 'Cell 6 Voltage']]
    file_v = open('Voltage_data.csv', 'a+', newline='')
    with file_v:
        write = csv.writer(file_v)
        write.writerows(D_v)

    # Writing Date and time of test to temperature data file
    file_t = open('Temperature_data.csv', 'a+', newline='')
    with file_t:
        write = csv.writer(file_t)
        write.writerows(D_t)

    Tend1 = t0+I.desired[0]
    Tend2 = t0+I.desired[1]+I.desired[0]
    Tend3 = t0+I.desired[2]+I.desired[1]+I.desired[0]
    Tend4 = t0+I.desired[3]+I.desired[2]+I.desired[1]+I.desired[0]
    t1 = 0

    while time.time() < Tend1:
        current_time = (round((time.time()-t0), 2))
        # Writing the voltage and temperature to each list
        rv = read_volts()
        V_store = [[current_time, rv[0], rv[1], rv[2], rv[3], rv[4], rv[5]]]

        # Storing Data on Voltage File
        file_V = open('Voltage_data.csv', 'a+', newline='')
        with file_V:
            write = csv.writer(file_V)
            write.writerows(V_store)

        Temperature = [[current_time, read_temp()]]
        # Storing Data on Temperature File
        file_T = open('Temperature_data.csv', 'a+', newline='')

        with file_T:
            write = csv.writer(file_T)
            write.writerows(Temperature)

        t1 = t1+1
        pause_time = (t1*(M.desired[0])+t0)-time.time()
        time.sleep(pause_time)

    t1 = 0
    while Tend1 < time.time() < Tend2:
        current_time = (round((time.time()-t0), 2))
        # Writing the voltage and temperature to each list
        rv = read_volts()
        V_store = [[current_time, rv[0], rv[1], rv[2], rv[3], rv[4], rv[5]]]
        # Storing Data on Voltage File
        file_V = open('Voltage_data.csv', 'a+', newline='')
        with file_V:
            write = csv.writer(file_V)
            write.writerows(V_store)

        Temperature = [[current_time, read_temp()]]
        # Storing Data on Temperature File
        file_T = open('Temperature_data.csv', 'a+', newline='')

        with file_T:
            write = csv.writer(file_T)
            write.writerows(Temperature)

        t1 = t1+1
        pause_time = (t1*(M.desired[1])+Tend1)-time.time()
        time.sleep(pause_time)

    t1 = 0
    while Tend2 < time.time() < Tend3:
        current_time = (round((time.time()-t0), 2))
        # Writing the voltage and temperature to each list
        rv = read_volts()
        V_store = [[current_time, rv[0], rv[1], rv[2], rv[3], rv[4], rv[5]]]
        # Storing Data on Voltage File
        file_V = open('Voltage_data.csv', 'a+', newline='')
        with file_V:
            write = csv.writer(file_V)
            write.writerows(V_store)

        Temperature = [[current_time, read_temp()]]
        # Storing Data on Temperature File
        file_T = open('Temperature_data.csv', 'a+', newline='')

        with file_T:
            write = csv.writer(file_T)
            write.writerows(Temperature)

        t1 = t1+1
        pause_time = (t1*(M.desired[2])+Tend2)-time.time()
        time.sleep(pause_time)

    t1 = 0
    while Tend3 < time.time() < Tend4:
        current_time = (round((time.time()-t0), 2))
        print(current_time)
        # Writing the voltage and temperature to each list
        rv = read_volts()
        V_store = [[current_time, rv[0], rv[1], rv[2], rv[3], rv[4], rv[5]]]
        # Storing Data on Voltage File
        file_V = open('Voltage_data.csv', 'a+', newline='')
        with file_V:
            write = csv.writer(file_V)
            write.writerows(V_store)

        Temperature = [[current_time, read_temp()]]
        # Storing Data on Temperature File
        file_T = open('Temperature_data.csv', 'a+', newline='')

        with file_T:
            write = csv.writer(file_T)
            write.writerows(Temperature)

        t1 = t1+1
        pause_time = (t1*(M.desired[3])+Tend3)-time.time()
        time.sleep(pause_time)


# For multiprocessing to work, the functions I am calling can not have input arguments
if __name__ == '__main__':
    p1 = Process(target=Read_Values)
    p1.start()
    p2 = Process(target=counter_V)
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
