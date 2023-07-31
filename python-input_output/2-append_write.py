#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """Appends a file using with"""
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
