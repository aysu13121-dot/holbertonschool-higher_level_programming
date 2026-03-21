#!/usr/bin/python3

def roman_to_int(roman_string):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return result

    previous = None
    for letter in roman_string:
        n = numbers[letter]

        if previous is None:
            result = n
            previous = n
            continue
        elif previous < n:
            result = result + n - previous * 2
        else:
            result += n

        previous = n

    return result
