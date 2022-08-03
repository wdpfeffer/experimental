from machine import Pin
import time

#define Pins for capacitive touch sensor
p_out = Pin(16, Pin.OUT)
p_in = Pin(4, Pin.IN)

p_out.off()
p_in.off()
print(p_out.value())
print(p_in.value())

time.sleep(5)

while True:
    start = time.ticks_us()
    p_out.on()
    while p_in.value() < 1:
        pass

    delta = time.ticks_diff(time.ticks_us(), start)
    print(f'Time diff (us): {delta}')
    p_out.off()
    time.sleep(5)
    


