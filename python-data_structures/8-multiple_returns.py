#!/usr/bin/python3
def multiple_returns(sentence:)

    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]

    lenght = len(sentence)
    tuple_result = (lenght, first_char)

    return tuple_result
