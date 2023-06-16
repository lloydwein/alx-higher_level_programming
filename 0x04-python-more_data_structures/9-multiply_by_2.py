#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
  Returns a new dictionary with all values multiplied by 2.

  Args:
    a_dictionary: The initial dictionary.

  Returns:
    A new dictionary with all values multiplied by 2.
  """

    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_value = 2 * value
        new_dictionary[key] = new_value

    return new_dictionary
