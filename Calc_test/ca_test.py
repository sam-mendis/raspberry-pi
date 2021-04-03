import time
from pymeasure.instruments.keithley import Keithley2400
import csv


keithley = Keithley2400("GPIB::1")
keithley.beep(100, 3)
time.sleep(10)
"Running Calcium Voltage measurements"

"Input desired current in Amps"
I = 1.875

"Input desired time of test in seconds"
T = 200

'Input Test Number and date e.g. V = [[1].[12/03/21]]'
V = [[1], []]

file_v = open('Voltage.csv', 'a+', newline='')
with file_v:
    write = csv.writer(file_v)
    write.writerows(V)


"Function to run"


def run():

    t0 = time.time()
    tend = t0+T
    keithley.apply_current()    # Sets up to source current
    keithley.ramp_to_current(I, steps=1, pause=0.02)  # Applies Source current

    while time.time() < tend:
        t = time.time()-t0

        # Measuring the voltage over the plate
        keithley.measure_voltage()
        v = keithley.voltage
        v1 = [[t], [v]]

        file_v = open('Voltage.csv', 'a+', newline='')
        with file_v:
            write = csv.writer(file_v)
            write.writerows(v1)
        time.sleep(20)


run()
