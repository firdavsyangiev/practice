'''OPERATORS & CONDITIONS
   (1) Operators
   (2) Conditions
   (3) Logical Operators   
'''

print("=====OPERATORS=======")
# + - > >= < <= * /   // % += **

a = 19
b = 5

result = a // b
left = a % b
print(f"Result: {result}, Left: {left}")

# a = a + 100
a = + 100
print("a:", a)

print("b**2:", b**2)
print("b**3:", b**3)

# print("a > b:", a > b)
# print("a * b:", a * b)
# print("a / b:", a / b)

print("="*10)

c = dict(name="Ray", age=24)
d = dict(name="Ray", age=24)
e = c

print("c == d:", c == d)  # only value
print(id(c), id(d), id(e))


print("c is d:", c is d)
print("c is e:", c is e)
