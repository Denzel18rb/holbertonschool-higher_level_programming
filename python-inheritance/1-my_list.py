#!/usr/bin/python3
"""we define the class mylist"""


class MyList(list):

    """print the list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
