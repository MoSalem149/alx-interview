#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """method determines if given data set represents a valid UTF-8 encoding"""
    num_bytes = 0
    for num in data:
        binary_rep = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for bit in binary_rep:
                if bit == '0':
                    break
                num_bytes += 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (binary_rep[0] == '1' and binary_rep[1] == '0'):
                return False
        num_bytes -= 1
    return num_bytes == 0
