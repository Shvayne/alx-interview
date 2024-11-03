#!/usr/bin/python3
"""This file contains a method that determines valid UTF-8 Encoding"""


def validUTF8(data):
    """This method checks if the variable 'data' is valid UTF-8"""
    num_bytes = 0

    # Masks for the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            mask = mask1
            while byte & mask:
                num_bytes += 1
                mask = mask >> 1

            # Single byte characters
            if num_bytes == 0:
                continue

            # Invalid number of bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
            
            # Adjust count since we're looking for continuation bytes
            num_bytes -= 1
        else:
            # Continuation byte must start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0