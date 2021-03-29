from temperature_sensor_code import measure_temp
from typing import AsyncContexstManager
import csv
import array
import json
import sys
import os
import glob
import math  # for creating time varying voltage and temperature maps
import time
from random import randint
from random import seed
from datetime import datetime
# For the GUI
from tkinter import *
from multiprocessing import Process
from gpiozero import LED, Button

# Importing and setting up keithley for measurements. Beep indicates code is interfacing with keithley
from pymeasure.instruments.keithley import Keithley2400
from smky import k_measure_v, k_measure_I, k_set_I, k_set_V
keithley = Keithley2400("GPIB::1")
keithley.beep(100, 3)
time.sleep(10)


# from temperature_sensor_code import *
# For the resetting
# for the time part
# For DS18B20
# Temperature sesnor is goig to be connected to GPIO 4


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

# Testing the code to see if it runs in parallel while checking lights etc


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


"Functions to open and close the relays on the MUX board"


def all_off():
    LED(2).off()  # Cell 1 (SDA)
    LED(3).off()  # Cell 2 (SCL)
    LED(17).off()  # Cell 3 (A_CS)
    LED(9).off()  # Cell 4 (MISO)
    LED(10).off()  # Cell 5 (MOSI)
    LED(8).off()  # Cell 6 (SCK)


def all_on():
    LED(2).on()
    LED(3).on()
    LED(17).on()
    LED(9).on()
    LED(10).on()
    LED(8).on()


def switch_on(n):
    R = [LED(2), LED(3), LED(17), LED(9), LED(10), LED(8)]
    R(n).on()


def switch_off(n):
    R = [LED(2), LED(3), LED(17), LED(9), LED(10), LED(8)]
    R(n).off()


# fake read temp


def read_temp():
    T = measure_temp()
    return T


def desired_temp():
    return 120


# The function to measure the voltage
def measure_volts():
    V = [0, 0, 0, 0, 0, 0]

    switch_on(1)
    time.sleep(0.3)
    V(0) = k_measure_v()
    time.sleep(0.5)
    switch_off(1)

    switch_on(2)
    time.sleep(0.3)
    V(1) = k_measure_v
    time.sleep(0.5)
    switch_off(2)

    switch_on(3)
    time.sleep(0.3)
    V(2) = k_measure_v
    time.sleep(0.5)
    switch_off(3)

    switch_on(4)
    time.sleep(0.3)
    V(3) = k_measure_v
    time.sleep(0.5)
    switch_off(4)

    switch_on(5)
    time.sleep(0.3)
    V(4) = k_measure_v
    time.sleep(0.5)
    switch_off(5)

    switch_on(6)
    time.sleep(0.3)
    V(5) = k_measure_v
    time.sleep(0.5)
    switch_off(6)

    return V


def set_volts(Input):
    'The function to set the keythlay voltages to what I want'
    print(Input)

# The Temperature controller which will run inside the function control


def temp_control(Temp):
    Temp.actualv(measure_temp())
    Temp.desiredv(desired_temp())

    if Temp.actual < Temp.desired:
        "switch on Heater by closing SSR"
        print('heater on(Switching GPIO 6 on)/or leaving on')
        # Switching GPIO 6 on
    else:
        '''switch off heater'''
        # Switching GPIO 6 off
    return Temp.actual


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
        rv = measure_volts()
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
        rv = measure_volts()
        V_store = [[current_time, rv[0], rv[1], rv[2], rv[3], rv[4], rv[5]]]

        # Storing Data on Voltage File
        file_V = open('Voltage_data.csv', 'a+', newline='')
        with file_V:
            write = csv.writer(file_V)
            write.writerows(V_store)

        # Storing Data on Temperature File
        Temperature = [[current_time, read_temp()]]

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
        rv = measure_volts()
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
        rv = measure_volts()
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
    p2 = Process(target=temp_control)
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
