from machine import Pin
from time import sleep

# Define the pin for TTP223B OUT pin is connected
touch_pin = Pin(4, Pin.IN)

while True:
    if touch_pin.value() == 1:
        print("Touch detected!")
    else:
        print("No touch detected.")
    
    sleep(0.2)