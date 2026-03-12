#!/usr/bin/python3
def no_c(my_string):
    result = []
    for char in my_string:
        if char != 'c' and char != 'C':
            result.append(char)
    retunr("".join(result))
