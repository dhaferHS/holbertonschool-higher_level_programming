#!/usr/bin/python3
"""
class empty rectangle
"""


class Rectangle:
    """
class empty Rectangle
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width


@property
def width(self):
    return self.__width


@width.setter
def widht(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    else:
        self.__widht = value


@property
def height(self):
    return self.__height


@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    else:
        self.__height = value
