from gpiozero import LED
from time import sleep

led = LED(17)  # using GPIO pin 17

# using a resistor of 10 kOhms

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
