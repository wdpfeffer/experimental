#main program, calling shift register function
import shiftc
import random
import utime

myshift = shiftc.shift()
myshift.shift_off()

while True:
    myshift.shift_update(random.getrandbits(3)+1)
    utime.sleep(0.05)