#!/usr/bin/python3
"""This file contains a method that determines valid UTF-8 Encoding"""
def validUTF8(data):
    """This method checks if the variable 'data' is valid UTF-8"""
    num_bytes = 0

    #masks for the leading bits
    mask1 = 1 << 7  #1000000
    mask2 = 1 << 6  #0100000

    for byte in data:
        #get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                #2byte character
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == mask1 >> 1:
                #3byte charcter
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == mask1 >> 2:
                #4byte character
                num_bytes = 3
            else:
                #invalid first byte
                return False
        else:
            #continuation byte must star with `10xxxxxx`
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1
  
    return num_bytes == 0