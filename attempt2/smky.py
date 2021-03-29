# My script to run the keythlay 2400 using raspberry pi
import pyvisa as visa
import time
from pymeasure.instruments.keithley import Keithley2400
from pymeasure.adapters import PrologixAdapter
import numpy as np
import pandas as pd


#adapter = PrologixAdapter('/dev/ttyUSB0')
#sourcemeter = Keithley2400(adapter.gpib(4))
keithley = Keithley2400("GPIB::1")


def k_measure_v():
    keithley.measure_voltage()

    V = keithley.voltage

    return V


def k_measure_i():
    keithley.measure_current()

    I = keithley.current

    return I


def k_set_V(v):
    keithley.apply_voltage()
    keithley.ramp_to_voltage(v, steps=1, pause=0.01)


def k_set_I(i):
    keithley.apply_current()
    keithley.ramp_to_current(i, steps=1, pause=0.01)
