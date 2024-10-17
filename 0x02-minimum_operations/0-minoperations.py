#!/usr/bin/python3
"""
    This file contains code to 
    calcualte the fewest number 
    of operations to get n*H characters
"""
def minOperations(n):
    """Calculate the min amount of operations required"""
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
