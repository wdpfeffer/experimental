
from machine import Pin
import utime
import random


class shift:
    
    
    def __init__(self, dp = 16, lp = 0, cp = 2):
        self.dataPIN = dp
        self.latchPIN = lp
        self.clockPIN = cp

        #set pins to output PIN objects
        self.dataPIN = Pin(self.dataPIN, Pin.OUT)
        self.latchPIN = Pin(self.latchPIN, Pin.OUT)
        self.clockPIN = Pin(self.clockPIN, Pin.OUT)
        
    #define shift register update function
    def shift_update(self, input):
        bs = ["00000001", "00000010", "00000100", "00001000", "00010000", "00100000", "01000000", "10000000"]
        
        if input==0:
            bsv = '00000000'
        else:
            bsv = bs[input-1]
        #put latch down to start data sending
        self.clockPIN.value(0)
        self.latchPIN.value(0)
        self.clockPIN.value(1)
      
        #load data in reverse order
        for i in range(7, -1, -1):
            self.clockPIN.value(0)
            self.dataPIN.value(int(bsv[i]))
            self.clockPIN.value(1)

        #put latch up to store data on register
        self.clockPIN.value(0)
        self.latchPIN.value(1)
        self.clockPIN.value(1)
        
    def shift_off(self):
        
        self.shift_update(0)

