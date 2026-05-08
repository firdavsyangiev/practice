print("=======numbers=======")
# in Java, variable is a name of storage location!
# in Python, variable is a name of object!

count = 100
count_type = type(count)
# print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("=======strings=======")
# METHODS: upper(), lower(), title(), replace(), find()
course = "AI Python Full Stack"
result = type(course)
print(f"the type of course: {result}")
result = course.title()
print(f"the result (1): {result}")

result = course.upper()
print(f"the result (2): {result}")

result = course.replace("Full Stack", "Masterclass")
print(f"the result (3): {result}")

print("=======booleans=======")
# function > type() input() bool() int() str()
y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY and FALSY values
# TRUTHY: True 100 -100 "MIT"
# FALSY: False 0  "" None

test_falsy = "" or False or 0 or None
print("The test_falsy:", bool(test_falsy))

test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))
1200
