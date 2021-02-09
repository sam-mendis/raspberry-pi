from multiprocessing import Process

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
