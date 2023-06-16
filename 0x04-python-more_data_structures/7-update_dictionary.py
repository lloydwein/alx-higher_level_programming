#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """function that replaces or adds key/value in a dictionary

    Args:
        a_dictionary: dictionnary
        key: key of the dictionnary
        value: value of the key

    Return:
        the dictionnary updated
"""

    a_dictionary[key] = value

    return a_dictionary
