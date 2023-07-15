#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord("a") <= ord(char) <= ord("z"):
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
            print("{}".format(result))
