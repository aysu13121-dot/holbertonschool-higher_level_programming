#!/usr/bin/pytohn3
"""This module defines a is_name_class function"""

def is_name_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class"""
    return type(obj) is a_class
