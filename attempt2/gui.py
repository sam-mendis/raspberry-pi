from random import randint
from random import seed
from datetime import datetime
# For the GUI
from tkinter import *
from multiprocessing import Process

# For the resetting
# for the time part
import time
import os
import sys
import json
import array
import csv
from typing import AsyncContextManager

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()

'''Sorting out date and time'''
date_time = datetime.now()
Date = '%s/%s/%s' % (date_time.day, date_time.month, date_time.year)
Time = '%s:%s:%s' % (date_time.hour, date_time.minute, date_time.second)


class parameters:

    def __init__(self, name):
        self.name = name
        self.value = float

    def values(self, value):
        self.value = value


# Assuming only working with 2 gases
A = parameters("Atmospheric Temperature")
# A.values(25)
T = parameters("Desired Temperature")
t = parameters('time in seconds')
g = parameters("Gas 1 Percentage")
V = parameters("Voltage to hold cells at")


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
