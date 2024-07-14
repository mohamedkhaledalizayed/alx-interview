#!/usr/bin/python3

"""
Module that contains a method that calculates
the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    operations = 0
    factor = 2

    if n < 0:
        return 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

        if factor * factor > n:
            if n > 1:
                operations += n
            break

    return operations
