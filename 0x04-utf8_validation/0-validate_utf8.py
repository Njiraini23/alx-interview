#!/usr/bin/python3
"""determines if dataset contains UTF-8 encoding"""


def validUTF8(data):
    """
    a method that determines if a given data set represents
    a valid UTF-8 encoding. returns True if data is a valid UTF-8
    else returns False. Character be 1 to 4 bytes long
    """
    n_bytes = 0

    for num in data:
        """check the data through the integers in the list"""
        byte = num & 0xFF

        if n_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                n_bytes -= 1
            else:
                return False

    return n_bytes == 0
