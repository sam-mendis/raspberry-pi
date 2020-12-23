from random import randint
from random import seed
# For the GUI
from tkinter import *


# For the resetting
# for the time part
import time
import os
import sys

# Importing Functions in functions.py
from functions import restart_program

from functions import v_measure
from functions import temp_control
from functions import temp_model
from functions import t_measure
from functions import start


# For the resetting
# for the time part

# Assuming voltage heat correlation is a linear model with m=50 and c = -30
# This model assumes atm = 20 and Vmeasured = 1 at Tatm

# need to have this before any tkinter program.
# this creates the window for the gui
root = Tk()


# Naming the Gui
root.title("Environmental Controller for Test Cell")
# Making an icon
# root.iconbitmap('control.png')

# Atmospheric Temperature
atm = 20


# Voltage at 120 deg C = 3V
# Voltage at 20 deg C = 1V


frame_s = Frame(root)
frame_s.grid()


# Creating the input table
inputlabel = Label(frame_s, text="Manual Input", font=" Times 16", width=35)
inputlabel.grid(row=0, column=0, columnspan=6)
templabel = Label(
    frame_s, text="Temp/\N{DEGREE SIGN}C", font=" Times 14", width=7)
templabel.grid(row=2, column=0)


timelabel = Label(frame_s, text="Time", bd=1, relief="solid",
                  font=" Times 14", width=26)
timelabel.grid(row=1, column=1, columnspan=3)
timelabeldays = Label(frame_s, text="Days", font=" Times 14", width=7)
timelabeldays.grid(row=2, column=1)
timelabelhours = Label(frame_s, text="Hours", font=" Times 14", width=7)
timelabelhours.grid(row=2, column=2)
timelabelmins = Label(frame_s, text="Minutes", font=" Times 14", width=7)
timelabelmins.grid(row=2, column=3)

gas1label = Label(frame_s, text="Gas A %", font=" Times 14", width=7)
gas1label.grid(row=2, column=4,)
gas2label = Label(frame_s, text="Gas B %", font=" Times 14", width=7)
gas2label.grid(row=2, column=5)

e_temp = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_temp.grid(row=3, column=0)

e_timed = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_timed.grid(row=3, column=1)
e_timeh = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_timeh.grid(row=3, column=2)
e_timem = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_timem.grid(row=3, column=3)

e_gas1 = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_gas1.grid(row=3, column=4)
e_gas2 = Entry(frame_s, bd=1, relief="solid", font=" Times 14", width=7)
e_gas2.grid(row=3, column=5)

# Creating a button, command calls the function next to command
# remember when using the command button not to but brackets after the function


# Here


def next():
    global temp_i, timed_i, timeh_i, timem_i, gasa_i, gasb_i
    temp_int = int(e_temp.get())

    timed_int = int(e_timed.get())
    timeh_int = int(e_timeh.get())
    timem_int = int(e_timem.get())

    time_s = timed_int*(86400)+timeh_int*(3600)+timem_int*(60)
    print(time_s)
    gasa_int = int(e_gas1.get())
    gasb_int = int(e_gas2.get())

    temp_i = (e_temp.get())
    timed_i = e_timed.get()
    timeh_i = e_timeh.get()
    timem_i = e_timem.get()
    gasa_i = (e_gas1.get())
    gasb_i = (e_gas2.get())

    frame_n = Frame(root)
    frame_n.grid()

    # Creating a restart if statement if Gas A + Gas B doesnt = 100%
    if (gasa_int+gasb_int) != 100:
        frame_s.destroy()
        error_g = Label(
            frame_n, text="Gas A & Gas B do not add up to 100%, please restart program")
        error_g.pack()
        restart = Button(frame_n, text="Restart", command=restart_program)
        restart.pack()

    # Creating a restart if statement if Gas A + Gas B doesnt = 100%
    if temp_int < atm or temp_int > 120:
        frame_s.destroy()
        atm1 = str(atm)
        error_t = Label(
            frame_n, text="Temperature is not within " + atm1 + "\N{DEGREE SIGN}C to 120\N{DEGREE SIGN}C")
        error_t.pack()
        restart = Button(frame_n, text="Restart", command=restart_program)
        restart.pack()

    templ = Label(frame_n, text="Temperature for Test")
    timel = Label(frame_n, text="Time for Test")
    gasl = Label(frame_n, text="Gas % s")
    tempinput = "Steady State Temp = " + temp_i + "\N{DEGREE SIGN}C"
    timeinput = timed_i + " Days " + timeh_i +\
        "H " + timem_i + "min"
    gasainput = "Gas A = " + gasa_i + "%, Gas B = " + gasb_i + "%"
    f_templabel = Label(frame_n, text=tempinput)
    f_timelabel = Label(frame_n, text=timeinput)
    f_gaslabel = Label(frame_n, text=gasainput)
    frame_s.destroy()
    templ.grid(row=1, column=1)
    timel.grid(row=1, column=2)
    gasl.grid(row=1, column=3)
    f_templabel.grid(row=2, column=1)
    f_timelabel.grid(row=2, column=2)
    f_gaslabel.grid(row=2, column=3)

    # Creating Start button
    button_start = Button(frame_n, text="Start", command=lambda: start(
        temp_int, time_s, gasa_int, atm))
    button_start.grid(row=3, column=4)

    # Creating a Clear Button
    button_clear = Button(frame_n, text="Clear", command=restart_program)
    button_clear.grid(row=1, column=4)


# creating a labels
button_next = Button(frame_s, text="Next", command=next)
button_next.grid(row=3, column=6)


root.mainloop()
