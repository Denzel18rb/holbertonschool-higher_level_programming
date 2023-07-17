#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        z = add(a, b)
        for x in range(4, 6):
            z = add(z, x)
        return z
    else:
        return sub(a, b)
