#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    novo_list = []
    for xyz in my_list:
        if xyz % 2 == 0:
            novo_list.append(True)
        else:
            novo_list.append(False)
    return novo_list
