import time
import pymeasure
import csv


#keithley = Keithley2400("GPIB::1")


"Running Calcium Voltage measurements"

"Input desired current in Amps"
I = 5

"Input desired time of test in seconds"
T = 10

'Input Test Number and date e.g. V = [[1].[12/03/21]]'
V = [[1], []]

#file_v = open('Voltage.csv', 'a+', newline='')
# with file_v:
#    write = csv.writer(file_v)
#    write.writerows(V)
print(V)


"Function to run"


def run():

    t0 = time.time()
    tend = t0+T
    # keithley.apply_current(I)    # Sets up to source current
    while time.time() < tend:
        t = 1
        # v = keithley.measure_voltage()  # Measuring the voltage over the plate
        V.append([[time.time()], [1]])
    print(V)


run()
