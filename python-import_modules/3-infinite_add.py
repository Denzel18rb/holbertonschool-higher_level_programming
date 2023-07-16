#!/usr/bin/python3
import sys

if __name__ == "__main__":
    leche = sys.argv[1:]
    azucar = sum(int(arg) for arg in leche)
    print(azucar)
