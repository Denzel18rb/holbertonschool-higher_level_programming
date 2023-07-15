#!/usr/bin/python3
def print_last_digit(number):
    lastn = abs(number) % 10
    print(lastn, end='')
    return lastn
