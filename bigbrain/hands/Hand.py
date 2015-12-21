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
        return Hand._Hand__readData(spi)
        

    @staticmethod
    def registerPalms(spi, name):
        """ change your identity-- the world is your oyster! """

        Hand._Hand__writeEnable(spi)
        Hand._Hand__eraseSector(spi)
        Hand._Hand__pageProgram(spi, name)
        Hand._Hand__writeDisable(spi)
        print 'Thanks for naming me ' + name

    @staticmethod
    def __readData(spi):
        # read instruction
        instruction = 0x03
        # sector address
        sector = 0x000000
        r = spi.xfer([instruction, sector])
        print r
        return r

    @staticmethod
    def __writeEnable(spi):
        # write enable instruction
        instruction = 0x06
        spi.xfer([instruction])
    
    @staticmethod
    def __writeDisable(spi):
        # write disable instruction
        instruction = 0x04
        spi.xfer([instruction])

    @staticmethod
    def __eraseSector(spi):
        # erase sector instruction
        instruction = 0x20
        sector = 0x000000
        spi.xfer([instruction, sector])

    @staticmethod
    def __pageProgram(spi, data):
        # convert data to hex
        data = map(ord, data)
        print data
        # page program instruction
        instruction = 0x02
        sector = 0x000000
        spi.xfer([instruction, sector] + data)

    def readHand(self):
        """ Read from ADC of individual hand. """
        pass
