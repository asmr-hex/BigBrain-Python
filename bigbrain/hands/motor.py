import time
import pkgutil
import spidev
import RPi.GPIO as GPIO

from bigbrain.hands import spp
from bigbrain.hands import cream
from bigbrain.hands.Hand import Hand

class Motor:
    """ Handles the detection and configuration of the controller
        system.
    """

    MAX_PLAYERS = 8
    # Define GPIO pins (BCM scheme) for custom chip selects
    _PORTS = {'lsb': 17,
              'mb' : 22,
              'msb': 23}
    _MODE = {'read':0, 'find':1}
    _SPI = None
    _handTypes = []

    def __init__(self):
        """ Initializes list of controller types available. """
        # Initialize GPIO ports
        GPIO.setmode(GPIO.BCM)
        for idx, pin in enumerate(self._PORTS.values()):
            # set pin to output mode and init low
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        # initialize SPI ports
        self._SPI = spidev.SpiDev()
        # Get available types of hands
        self._handTypes = [hand for imp, hand, ispkg in pkgutil.iter_modules(spp.__path__)]
        print self._handTypes

    def findHands(self):
        """ Scan for controllers. """
        # Open SPI device for find mode
        self._SPI.open(0, self._MODE['find'])
        # Scan each identity port (ports 0-7, CS 1)
        for port in xrange(0, self.MAX_PLAYERS):
            # select a port
            self.__select_port(port)
            # read value at port (TODO: talk to SPI flash IC)
            #data = self._readADC(0)
            # check for a known hand type.
            identity = Hand.readPalms(self._SPI)
            time.sleep(0.5)
            

    def readHands(self):
        """ Read bits from active ports. """
        print "HERE"
        # open SPI device for read more
        self._SPI.open(0, self._MODE['read'])
        # scan each identity port (ports 0-7, CS 0)
        for port in xrange(0, self.MAX_PLAYERS):
            # select a port
            self.__select_port(port)
            data = self._readADC(0)
            time.sleep(0.5)

    def nameHand(self, p, name):
        """ give/change the name of this poor hand on port p! """
        # open SPI device for find mode
        self._SPI.open(0, self._MODE['find'])
        # select a port
        self.__select_port(p)
        #self.__writeEnable()
        #print "hooray"
        Hand.registerPalms(self._SPI, name)


    def __writeEnable(self):
        # write enable instruction
        instruction = 6
        self._SPI.xfer2([instruction])
    

    def __writeDisable(self):
        # write disable instruction
        instruction = 4
        self._SPI.xfer2([instruction])

    def __eraseSector(self):
        # erase sector instruction
        instruction = 0x20
        sector = 0xFFFFFF
        self._SPI.xfer([instruction, sector])

    def __pageProgram(self, data):
        # page program instruction
        instruction = 0x02
        sector = 0xFFFFFF
        self._SPI.xfer([instruction, sector, data])


    def _readADC(self, nADC):
        if (nADC > 7) or (nADC < 0):
            return -1
        r = self._SPI.xfer([1, (8+nADC)<<4, 0])
        out = ((r[1]&3) << 8) + r[2]
        return out

    def __select_port(self, n):
        """ selects a port.

        Using an int in [0-7], activte the chip select for
        device n.

        Args:
            n (int): the port corresponding to the device to activate.
        """
        # convert int to its binary representation.
        msb, mb, lsb = cream.num2bin(n)
        # set GPIOs to output bit pattern.
        GPIO.output(self._PORTS['msb'], msb)
        GPIO.output(self._PORTS['mb'], mb)
        GPIO.output(self._PORTS['lsb'], lsb)        
        
        
