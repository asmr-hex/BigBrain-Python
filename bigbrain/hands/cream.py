# Cream is applied gently to each hand, promoting health and
# productivity.
#
# A collection of helpers to make life easier.

def num2bin(n):
    """ Converts a number into its binary representation.
        The range of the representation is constraints to
        3 bits (0-7) base 10.

        :param n:   int between 0 and 7
        :returns msb,mb,lsb:    most-significant-bit,
                                middle-bit,
                                least-significant-bit
    """
    if n < 0 or n > 7:
        raise ValueError("int must be within range!")
    msb = (n & 4) >> 2
    mb = (n & 2) >> 1
    lsb = (n & 1)
    return msb, mb, lsb
