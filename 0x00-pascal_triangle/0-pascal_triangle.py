#!/usr/bin/python3
"""
    This module contains code that returns a pascal triangle
    calculated using the binomial coefficient
"""
def pascal_triangle(n):
    """
        Returns a list of integers representing the
        pascal triangle of n
    """
    if n <= 0:
        return []
    
    result = []
    for i in range(n):
        row = [1]
        for k in range(1, i + 1):
            next_value = row[k - 1] * (i - (k - 1)) // k #binomial coefficient
            row.append(next_value)
        result.append(row)
    return result