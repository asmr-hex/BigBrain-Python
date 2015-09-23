  
import spidev
import RPi.GPIO as GPIO
import time

NPlayers = 8

#Define GPIO Pins for CS
A = 17
B = 22
C = 23
pins = [A, B, C]
vals = [0, 0, 0]

GPIO.setmode(GPIO.BCM)
for idx, pin in enumerate(pins):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, vals[idx])


#Test SPI transactions

spi = spidev.SpiDev()
spi.open(0,0)

def readADC(nADC):
    if (nADC > 7) or (nADC < 0):
        return -1
    r = spi.xfer2([1, (8+nADC)<<4, 0])
    out = ((r[1]&3) << 8) + r[2]
    return out

while True:
    D = [0, 0]
    for n in xrange(0, 2):
        D[n] = readADC(n)
    print "\tUP: " + str(D[0]) + "\tRIGHT: " + str(D[1])
    time.sleep(0.5)







#Loop over outputs
try:
    i = 0
    while True:
        if i >= NPlayers:
            i = 0
        vals[0] = (i & 1)
        vals[1] = (i & 2) >> 1
        vals[2] = (i & 4) >> 2
        for idx, pin in enumerate(pins):
            GPIO.output(pin, vals[idx])
        print str(i) + " = " + str(vals[2]) + str(vals[1]) + str(vals[0])
        time.sleep(0.4)
        i+=1
except KeyboardInterrupt:
    GPIO.cleanup()

