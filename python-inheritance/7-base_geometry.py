#!/usr/bin/python3
"""This  module defines base goemetry class"""


class BaseGeometry:
    """A class that defines base geometry"""

    def area(self):
        """Raises an Exception - area() is not implemented"""
        raise Exceptions("area() is not implement")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
