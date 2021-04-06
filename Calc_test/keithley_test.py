import time
from pymeasure.instruments.keithley import Keithley2400


keithley = Keithley2400("GPIB::1")
keithley.beep(100, 5)
time.sleep(10)

keithley.beep(100, 5)

print("If buzzer sounds, keithley works with pi")
