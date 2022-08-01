#!/usr/bin/python3
"""
Minumum operation Model
"""


def minOperations(n):
   
    if type(n) is not int or n < 2:
        return 0
    result = 0
    iteration = 2
    while n > 1:
        if n % iteration == 0:
            result += iteration
            n /= iteration
        else:
            iteration += 1
    return result