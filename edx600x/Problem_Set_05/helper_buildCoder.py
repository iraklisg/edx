import string
import random

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    uppercase_letters = string.ascii_uppercase # A string that contains all uppercase letters in order
    lowercase_letters = string.ascii_lowercase # A string that contains all lowercase letters in order
    length_upper = len(uppercase_letters)
    length_lower = len(lowercase_letters)
    # create uppercase cipher {key:value} such as dict = {string[i]:string[i+shift] if i < len(string)-shift else string[i+shift-len(string)] for i in range(len(string))}
    # In general, dict comprehension: {(some_key if some_condition==True else other_key) : (some_value if some_condition==True else other_value), for some_range_of_values }
    # Example 1: { (some_key if condition else default_key):(something_if_true if condition else something_if_false) for key, value in dict_.items() }
    # Example 2: { (some_string[i] if i > 10 else some_string[i+1]):(some_other_string[i] if i > 5 else some_other_string[i+1]) for i in some_range }  
    # Example 3: d is a {key:some_dictionary.get(key, 0) for key in some_range}
    dict_upper = {uppercase_letters[i] : uppercase_letters[i+shift] if i < length_upper-shift else uppercase_letters[i+shift-length_upper]  for i in range(length_upper)}
    # create lowercase cipher
    dict_lower = {lowercase_letters[i] : lowercase_letters[i+shift] if i < length_lower-shift else lowercase_letters[i+shift-length_lower]  for i in range(length_lower)}
    # Built cipher dictionary by merging dict_upper and dict_lower:
    # In general: merge dictionaries x, y into dictionary z : z = dict(x.items() + y.items())
    cipher = dict(dict_upper.items() + dict_lower.items())
    return cipher
