#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
     Input data: a list of integers
     Return: Bool if data is a valid UTF-8 encoding
     A character in UTF-8 can be 1 to 4 bytes long
     The data set can contain multiple characters
    """
    n_bytes = 0

    for num in data:
        """iterating throu each int num in the data list"""
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
