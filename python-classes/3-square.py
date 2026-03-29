#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """represent a square"""
    def __init__(self, siz=0):
        """Initialize a new Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
