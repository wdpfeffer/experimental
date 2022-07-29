import network
from machine import Pin

p_int = Pin(2, Pin.OUT)

method = 'utf-8'

wlan = network.WLAN(network.STA_IF)
if not wlan.active():
    wlan.active(True)
    
scans = wlan.scan()
if len(scans)> 1:
    #sort scans by signal strength
    p_int.off()
    scans.sort(key = lambda x: x[3], reverse = True)
    for scan in scans:
        try:
            nsize = len(scan[0].decode(method))
            if nsize > 0 and (-100 < scan[3] and scan[3] < 0):
                print(f'name size: {nsize} name: {scan[0].decode(method)}, strength: {scan[3]}')
        except:
            print('error')
            pass
    
    p_int.on()
        

    