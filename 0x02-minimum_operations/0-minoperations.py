#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations
needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.
    
    :param n: Target number of H characters
    :type n: int
    :return: Minimum number of operations or 0 if n is impossible to achieve
    :rtype: int
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
