# object orientated programming example
import csv
import time
from datetime import datetime
from multiprocessing import Process
import time


class parameters:

    def __init__(self, name, input, value):
        self.name = name
        self.input = input
        self.value = value

    def input_v(self):
        return self.input

    def reading(self, value, file, time):
        self.value = value
        with file:
            write = csv.writer(file)
            write.writerows([[time, value]])

    def change(self, input):
        self.input = input


"Input parameters for test below"
# Total test time is the input, reading is current time
Time = parameters("Time", 100, 0)
Temp = parameters("Temp", [100, 50, 100, 50], )
Volts = parameters("Voltage", 1, [])
Interval = parameters("Measurement Interval", [15, 30, 45, 60], )  # In minutes
Period = parameters("Time period that each specific interval will occur", [
                    25, 50, 75, 100], )  # In hours


'''Sorting out date and time'''
date_time = datetime.now()
Date = '%s/%s/%s' % (date_time.day, date_time.month, date_time.year)
Current_Time = '%s:%s:%s' % (
    date_time.hour, date_time.minute, date_time.second)


def measure_temp():

    output = 50
    print(output)
    return output


def measure_voltage():

    output = 20
    print(output)
    return output


def set_voltage(volts):

    pass


def temp_control():
    t0 = time.time()
    t = 0
    while t < Period.input[0]:
        current_temp = measure_temp
        if current_temp < Temp.input[0]:
            print("Switch On SSR")
        else:
            print("Switch Off SSR")
        t = (time.time()-t0)/3600

    while t < Period.input[1]:
        current_temp = measure_temp
        if current_temp < Temp.input[1]:
            print("Switch On SSR")
        else:
            print("Switch Off SSR")
        t = (time.time()-t0)/3600

    while t < Period.input[2]:
        current_temp = measure_temp
        if current_temp < Temp.input[2]:
            print("Switch On SSR")
        else:
            print("Switch Off SSR")
        t = (time.time()-t0)/3600

    while t < Period.input[3]:
        current_temp = measure_temp
        if current_temp < Temp.input[3]:
            print("Switch On SSR")
        else:
            print("Switch Off SSR")
        t = (time.time()-t0)/3600


def store_values():
    t0 = time.time()
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

    Tend1 = t0+(Period.input[0]*3600)
    Tend2 = t0+(Period.input[1]*3600)
    Tend3 = t0+(Period.input[2]*3600)
    Tend4 = t0+(Period.input[3]*3600)
    t1 = 0

    while time.time() < Tend1:
        current_time = (round((time.time()-t0), 2))
        Temp.reading(measure_temp, file_t, current_time)
        Volts.reading(measure_voltage, file_v, current_time)
        set_voltage(Volts.input[0])
        t1 = t1+1
        pause = (t1*Interval.input[0]*60)+t0 - time.time()
        time.sleep(pause)
    t1 = 0
    while time.time() < Tend2:
        current_time = (round((time.time()-t0), 2))
        Temp.reading(measure_temp, file_t, current_time)
        Volts.reading(measure_voltage, file_v, current_time)
        set_voltage(Volts.input[1])
        t1 = t1+1
        pause = (t1*Interval.input[1]*60)+t0 - time.time()
        time.sleep(pause)

    t1 = 0
    while time.time() < Tend3:
        current_time = (round((time.time()-t0), 2))
        Temp.reading(measure_temp, file_t, current_time)
        Volts.reading(measure_voltage, file_v, current_time)
        set_voltage(Volts.input[2])
        t1 = t1+1
        pause = (t1*Interval.input[2]*60)+t0 - time.time()
        time.sleep(pause)

    t1 = 0
    while time.time() < Tend4:
        current_time = (round((time.time()-t0), 2))
        Temp.reading(measure_temp, file_t, current_time)
        Volts.reading(measure_voltage, file_v, current_time)
        set_voltage(Volts.input[3])
        t1 = t1+1
        pause = (t1*Interval.input[3]*60)+t0 - time.time()
        time.sleep(pause)


if __name__ == '__main__':
    p1 = Process(target=store_values)
    p1.start()
    p2 = Process(target=temp_control)
    p2.start()
    p1.join()
    p2.join()
