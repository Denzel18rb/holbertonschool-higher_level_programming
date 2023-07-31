#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherit from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """area method that return area of the square"""
        return super().area()

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
