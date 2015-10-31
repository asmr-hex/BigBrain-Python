import time
import pkgutil
import spidev
import RPi.GPIO as GPIO

from BigBrain.hands import spp
import BigBrain.hands.cream

class Motor:
    """ Handles the detection and configuration of the controller
        system.
    """

    MAX_PLAYERS = 8
    # Define GPIO pins (BCM scheme) for custom chip selects
    _PORTS = {'msb': 17,
              'mb' : 22,
              'lsb': 23}
    _MODE = {'read':0, 'find':1}
    _SPI = None
    _handTypes = []

    def __init__(self):
        """ Initializes list of controller types available. """
        # Initialize GPIO ports
        GPIO.setmode(GPIO.BCM)
        for idx, pin in enumerate(self._PORTS.values()):
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        # Initialize SPI ports
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
            # Select a port
            msb, mb, lsb = cream.num2bin(port)
            GPIO.output(self._PORTS['msb'], msb)
            GPIO.output(self._PORTS['mb'], mb)
            GPIO.output(self._PORTS['lsb'], lsb)
            # Read value at port (TODO: talk to SPI flash IC)

    def readHands(self):
        """ Read bits from active ports. """
        pass


