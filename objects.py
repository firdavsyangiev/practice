''' OBJECTS
    (1) What is an object?
    (2) Iterable objects and RANGE
    (3) DICTIONARIES  
    (4) Error handling system
'''

import array  # package/module
import math  # package
from math import ceil
print("=====What is an object?=======")
# An object has state and method propeerties.
# Everything in Python is an object.

print(type('Hello World'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & Object Oriented Programming (OOP)
# OOP 4 concepts: Encapsulation | Abstraction | Inheritance | Polymorphism
result1 = math.ceil(96.7)  # CALL
print("Result1:", result1)

result2 = math.ceil(98.7)  # CALL
print("Result2:", result2)
