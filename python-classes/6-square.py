#!/usr/bin/python3
""" Printing a square """


class Square:
    """class square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialsation"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """size"""
        return self.__size

    @property
    def position(self):
        """position"""
        return self.__position

    @size.setter
    def size(self, value):
        """size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """value"""
            self.__size = value

    @position.setter
    def position(self, value):
        """position"""
        if type(value) != tuple or len(value) != 2 or \
            type(value) != int or value[0] < 0 or \
            type(value) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """printing"""
        if self.__size > 0:
            if self.position[1] > 0:
                print("\n" * self.position[1], end="")
            for i in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print(end="\n")