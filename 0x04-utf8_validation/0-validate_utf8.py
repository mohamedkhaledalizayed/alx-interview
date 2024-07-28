#!/usr/bin/python3
"""this file contain a method that determines if a given
data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding or not.

    Args:
      data : list of integers,
            each integer represents byte encoding in utf-8.
    Return:
      bool : True if valid utf otherwise False.

    """
    n_bits = 0
    for num in data:
        if n_bits > 0:
            # check the msb is 1 and 7th bit is 0
            if ((num >> 6) & 0b11) == 0b10:
                n_bits -= 1
            else:
                return False
        elif ((num >> 7) & 1) == 0:
            continue
        else:
            if ((num >> 3) & 0b11111) == 0b11110:
                n_bits = 3
            elif ((num >> 4) & 0b1111) == 0b1110:
                n_bits = 2
            elif ((num >> 5) & 0b111) == 0b110:
                n_bits = 1
            else:
                return False
    return True if n_bits == 0 else False
