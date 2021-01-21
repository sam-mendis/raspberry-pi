# Writing functions to call in attempt 1
# For the resetting
import sys
import os
import json
import csv
# for the time part
import time
import numpy as np
from random import seed
from random import randint
from multiprocessing import Process
import multiprocessing as mp


# Temperature modeling for feedback
def model_temp(T):
    global temp_f
    temp_f = T/(0.9)
    return temp_f

# Writing a function to restart the program if there is an error


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# 1 in logbook model


def v_measure(V2):
    T1 = V2*(50)-30
    return T1

# 2 in the logbook model


def temp_control(temp, input):

    V = (temp-input)*(0.3)
    return V

# 3 in the logbook model


def temp_model(V, current_temp):
    output = V+current_temp
    return output

# 4 in the logbook model


def t_measure(Tout):
    voltage = (Tout+28)/50
    return voltage


def cells_measure(Time, t_end):
    # Remeber time is in seconds!
    # Set GPIO's to whatever state they need to be
    Cell_1 = []
    Cell_2 = []
    Cell_3 = []
    Cell_4 = []
    Cell_5 = []
    Cell_6 = []
    t0 = time.time()
    print('Working')
    if Time < 3600:
        while time.time() < t_end:
            TT = 6  # every 6 minutes we want the thing to run again
            running = (time.time()-t0)/60
            count = running % TT
            if count == 0:
                ''' Cell 1 '''
                time.sleep(5)
                # change gpio output
                print("changing gpio for cell 1 output")
                time.sleep(20)
                # measure voltage and current 1
                A1 = 0.3

                time.sleep(5)
                # measure voltage and current 2
                A2 = 0.3
                time.sleep(5)
                # measure voltage and current 3
                A3 = 0.3

                Cell_1.append((A1+A2+A3)/3)
                # switch of gpio zero

            if count == 1:
                ''' Cell 2 '''
                time.sleep(5)
                # change gpio output
                print("changing gpio for cell 2 output")
                time.sleep(20)
                # measure voltage and current 1
                A1 = 0.3

                time.sleep(5)
                # measure voltage and current 2
                A2 = 0.3
                time.sleep(5)
                # measure voltage and current 3
                A3 = 0.3

                Cell_2.append((A1+A2+A3)/3)
                # switch of gpio zero
            if count == 2:
                ''' Cell 3 '''
                time.sleep(5)
                # change gpio output
                print("changing gpio for cell 3 output")
                time.sleep(20)
                # measure voltage and current 1
                A1 = 0.3

                time.sleep(5)
                # measure voltage and current 2
                A2 = 0.3
                time.sleep(5)
                # measure voltage and current 3
                A3 = 0.3

                Cell_3.append((A1+A2+A3)/3)
                # switch of gpio zero
            if count == 3:
                ''' Cell 4 '''
                time.sleep(5)
                # change gpio output
                print("changing gpio for cell 4 output")
                time.sleep(20)
                # measure voltage and current 1
                A1 = 0.3

                time.sleep(5)
                # measure voltage and current 2
                A2 = 0.3
                time.sleep(5)
                # measure voltage and current 3
                A3 = 0.3

                Cell_4.append((A1+A2+A3)/3)
                # switch of gpio zero
            if count == 4:
                ''' Cell 5 '''
                time.sleep(5)
                # change gpio output
                print("changing gpio for cell 5 output")
                time.sleep(20)
                # measure voltage and current 1
                A1 = 0.3

                time.sleep(5)
                # measure voltage and current 2
                A2 = 0.3
                time.sleep(5)
                # measure voltage and current 3
                A3 = 0.3

                Cell_5.append((A1+A2+A3)/3)
                # switch of gpio zero

            if count == 5:
                ''' Cell 6 '''
                time.sleep(5)
                # change gpio output
                print("changing gpio for cell 6 output")
                time.sleep(20)
                # measure voltage and current 1
                A1 = 0.3

                time.sleep(5)
                # measure voltage and current 2
                A2 = 0.3
                time.sleep(5)
                # measure voltage and current 3
                A3 = 0.3

                Cell_6.append((A1+A2+A3)/3)
                # switch of gpio zero

    if 3600 <= Time < (5*86400):
        TT = 30

    if (5*86400) <= Time < 10*(86400):
        TT = 60

    if (10*86400) <= Time:
        TT = 120
    print(Cell_2)


def t_control(temp, T2, t_end, count):
    while time.time() < t_end:
        V1 = temp_control(temp, T2)
        T1 = temp_model(V1, T2)
        V2 = t_measure(T1)
        T2 = v_measure(V2)
        current_temp = str(round(T2, 1))
        count = count + 1
        t_print = str(count*3)
        T_a.append(current_temp)
        print("Temp at Time " + t_print + "s = " + current_temp)

        time.sleep(3)
    print(T_a)


def start(temp, seconds, gasa, atm):

    current_temp = atm
    t_end = time.time() + seconds
    T2 = atm
    count = 0
    print(T2)
    t1 = int(seconds/3)
    global T_a
    T_a = [atm]

    print(t_end)
    #a = t_control(temp, T2, t_end, count)
    # print(a)
    if __name__ == 'functions':
        p1 = Process(target=t_control(temp, T2, t_end, count))
        p1.start()
        p2 = Process(target=cells_measure(seconds, t_end))
        p2.start()
        p1.join()
        p2.join()
