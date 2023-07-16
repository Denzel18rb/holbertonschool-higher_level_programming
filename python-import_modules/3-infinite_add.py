#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    leche = len(argv)
    azucar = 0
    for i in range(1, leche):
        azucar += int(argv[i])
        print("{:d}".format(azucar))
