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
