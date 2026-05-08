# Dunder __builtins__, __init__
message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Pythin, there are built-in tools:
(1) TYPES > int, float, str, list, dict, 
(2) FUNCTION > print(), len(), input(), type()
(3) CONSTANTS > True, False, None
'''

print(dir(__builtins__))
