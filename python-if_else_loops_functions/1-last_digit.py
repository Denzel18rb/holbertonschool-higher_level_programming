#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 0:
    digit = (-number) % 10
    digit = -digit
if number % 10 == 0:
    print(f"Last digit of {number} is {digit} and is 0")
elif number % 10 < 6:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
elif number % 10 > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
