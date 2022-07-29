
def do_connect():
    import time
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('1-FBIsurveillance', 'tInKtHEGoAt06')
        count=0
        while not wlan.isconnected():
            count+=1
            print('Loop count = {}'.format(count))
            if count > 30:
                print('Could not connect to network')
                break
            time.sleep(1)
    if wlan.isconnected():        
        print('network config:', wlan.ifconfig())
    
# Connect to wireless network    
do_connect()