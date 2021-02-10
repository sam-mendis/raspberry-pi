'''from multiprocessing import Process

import time
global x
x = 0


def test1():

    global x
    x = 1


def test2():
    t = 0
    while t < 5:
        if x == 0:
            print("it hasnt worked")
        if x == 1:
            print("It has worked")

        t = t+1
        time.sleep(1)


if __name__ == '__main__':
    p1 = Process(target=test1)
    p1.start()
    p2 = Process(target=test2)
    p2.start()
    p1.join()
    p2.join()
'''
import csv
Cells_V = [[0, 0], [
    'Time in seconds/s', 'Cell 1 Voltage/V', 'Cell 2 Voltage/V', 'Cell 3 Voltage/V', 'Cell 4 Voltage/V', 'Cell 5 Voltage/V', 'Cell 6 Voltage/V'], [0, 0, 0, 0, 0, 0, 0]]


def read_volts():
    # Some function to measure the voltage of each cell

    V = [0, 0, 0, 0, 0, 0]
    V[0] = V[0]+1
    V[1] = V[1]+1
    V[2] = V[2]+1
    V[3] = V[3]+1
    V[4] = V[4]+1
    V[5] = V[5]+1
    return V


V = read_volts()
print(V)
Cells_V.append([10, V[0], V[1], V[2], V[3], V[4], V[5]])
print(Cells_V)


file = open('Temperature_data.csv', 'a+', newline='')

with file:
    write = csv.writer(file)
    write.writerows(Cells_V)
