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


print("=====Error Handling System=======")

''' ERROR:
car_dict = dict(name="Toyota", year=2026, electric=True)
result = car_dict["origin"]  
print("Result:", result)
'''

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("PASSED HERE")
    a = car_dict.speed
    result = car_dict["origin"]
    print("Result:", result)
# except KeyError as err:
#     print("No origin state property found:", err)
# except AttributeError as err:
#     print("No speed attribute found:", err)
# except (KeyError, AttributeError) as err:
#     print("Error:", err)
except Exception as err:
    print("General Error:", err)
else:
    print("Executed successfully without any error.")
finally:
    print("Final closing logic")
