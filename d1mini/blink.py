from machine import Pin
import time

p = Pin(2, Pin.OUT)

while True:
    if p.value():
        p.value(0)
    else:
        p.value(1)
    
    time.sleep(1)
