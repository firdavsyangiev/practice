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


print("c is d:", c is d)  # only reference
print("c is e:", c is e)


print("=====CONDITIONS=======")
x = 5

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("====== LOGICAL OPERATORS ======")

# age = 18
# person = None

# if age > 18:
#     person = "Adult"
# else:
#     person = "Child"

# print("Person:", person)


# Ternary operator
age = 18

person = "Adult" if age >= 18 else "Minor"
print("Person:", person)

print("============")

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("hi, Do you want to be a student?")
elif is_admin:
    print("Please,go to the office")
# elif is_guest or is_parent:
elif is_guest and is_parent:
    print("Waiting room is over here!")
else:
    print("Other case")
