#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    hueso = len(argv) - 1
    if hueso == 0:
        print("{}".format("0 arguments."))
    elif hueso == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(hueso, "arguments:"))
        for i in range(1, hueso + 1):
            print("{:d}: {}".format(i, argv[i]))
