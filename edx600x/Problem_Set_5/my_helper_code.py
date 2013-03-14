import string
import random

uppercase_letters = string.ascii_uppercase # A string that contains all uppercase letters in order
lowercase_letters = string.ascii_lowercase # A string that contains all lowercase letters in order

# { (some_key if condition else default_key):(something_if_true if condition else something_if_false) for key, value in dict_.items() }

print uppercase_letters
shift = 3
length_upper = len(uppercase_letters)
length_lower = len(lowercase_letters) 
dict_upper = {uppercase_letters[i] : uppercase_letters[i+shift] if i < length_upper-shift else uppercase_letters[i+shift-length_upper]  for i in range(length_upper)}
print dict_upper

dict_lower = {lowercase_letters[i] : lowercase_letters[i+shift] if i < length_lower-shift else lowercase_letters[i+shift-length_lower]  for i in range(length_lower)}
print dict_lower

# merge dictionaries x, y into dictionary z : z = dict(x.items() + y.items())
cipher = dict(dict_upper.items() + dict_lower.items())
print cipher