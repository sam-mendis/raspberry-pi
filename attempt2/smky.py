# My script to run the keythlay 2400 using raspberry pi
import pyvisa as visa
import time
from pymeasure.instruments.keithley import Keithley2400
from pymeasure.adapters import PrologixAdapter
import numpy as np
import pandas as pd


#adapter = PrologixAdapter('/dev/ttyUSB0')
#sourcemeter = Keithley2400(adapter.gpib(4))
