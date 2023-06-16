#!/usr/bin/python3
"""function that deletes keys with a specific value in a dictionary

    Args:
        a_dictionary: dictionary
        value: value of the dictionary to deleted

    Return:
        the dictionary updated
"""


def complex_delete(a_dictionary, value):
    for i in list(a_dictionary):
        if a_dictionary[i] == value:
            del a_dictionary[i]

    return a_dictionary
