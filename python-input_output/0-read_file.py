#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """Reads a file using with"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end='')
