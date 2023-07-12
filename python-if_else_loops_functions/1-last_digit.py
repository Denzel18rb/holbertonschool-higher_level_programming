#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if digit == 0:
    print("last digit of {} is {} and is 0".format(number, digit))
elif digit > 5:
    print("last digit of {} is {} and is greater than 5".format(number, digit))
elif digit < 6:
    print("last digit of {} is {} less than 6 and not 0".format(number, digit))
