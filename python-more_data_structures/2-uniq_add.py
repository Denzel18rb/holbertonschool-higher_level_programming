#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    firstset = set(my_list)
    for num in firstset:
        sum += num
    return sum
