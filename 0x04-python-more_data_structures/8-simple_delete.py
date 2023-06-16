#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """function that deletes a key in a dictionary

    Args:
        a_dictionary: dictionnary
        key: key of the dictionnary to deleted

    Return:
        the dictionnary updated
"""


    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
