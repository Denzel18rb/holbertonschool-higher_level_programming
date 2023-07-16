#!/usr/bin/python3
def no_c(my_string):
    novo_str = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            novo_str += letter
    return novo_str
