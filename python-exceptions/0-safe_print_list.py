#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    try:
        for z in range(x):
            print("{}".format(my_list[z]), end="")
            z += 1
        print("")
    except IndexError:
        print("")
    return z
