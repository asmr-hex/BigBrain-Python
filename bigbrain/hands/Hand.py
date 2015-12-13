import spidev
import RPi.GPIO as GPIO

class Hand:
    """ Abstract class for controllers. """

    def __init__(self):
        """ stuff. """
        pass

    @staticmethod
    def readPalms(spi):
        """ decipher the true identity of that spooky hand
        at port p!
        """
        print "BOO"

    @staticmethod
    def registerPalms(spi, name):
        """ change your identity-- the world is your oyster! """
        Hand._Hand__writeEnable(spi)
        print 'Thanks for naming me ' + name

    @staticmethod
    def __writeEnable(spi):
        print
        #spi.xfer([
        pass 

    def readHand(self):
        """ Read from ADC of individual hand. """
        pass
