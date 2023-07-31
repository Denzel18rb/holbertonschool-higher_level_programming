#!/usr/bin/python3
"""
Student to JSON
"""


class Student:
    """defines a studend"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            new_dict = {}
            for k in self.__dict__:
                for k2 in attrs:
                    if k == k2:
                        new_dict[k] = self.__dict__[k]
            return new_dict
        else:
            return self.__dict__
