# Writing functions to call in attempt 1
# For the resetting
import sys
import os
# for the time part
import time

from random import seed
from random import randint


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


def start(temp, seconds, gasa, atm):

    current_temp = atm
    t_end = time.time() + seconds
    T2 = atm
    print(T2)
    print(t_end)
    while time.time() < t_end:
        V1 = temp_control(temp, T2)
        T1 = temp_model(V1, T2)
        V2 = t_measure(T1)
        T2 = v_measure(V2)
        current_temp = T2
        print(current_temp)
        time.sleep(3)
