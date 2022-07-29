#main program, calling shift register function
import shift
import random
import utime

bit_string="00000000"
bs = ["00000000","00000001","00000010","00000100","00001000","00010000",
      "00100000","01000000", "10000000"]

shift.shift_update(bit_string,shift.dataPIN,shift.clockPIN,shift.latchPIN)

while True:
    shift.shift_update(bs[random.getrandbits(3)],shift.dataPIN,shift.clockPIN,shift.latchPIN)
    utime.sleep(0.3)