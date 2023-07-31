#!/usr/bin/python3
"""
define a my list.
"""


class MyList(list):
    """
    class list.
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
