#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize a new square

        args:
            size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value


    def area(self):
        """Return the current area of the square"""
        return(self.__size * self.__size)


