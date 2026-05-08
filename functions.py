''' FUNCTIONS
(1) DEFINE & CALL
(2) ARGUMENTS & PARAMETERS
(3) KEYWORD & DEFAULT ARGUMENTS
(4) SCOPE
'''

print("======= DEFINE & CALL ========")
# built-in function: print() type()
# Function - reusable block of code
# Instead of block {} in JAVA, PYHTON uses indentation

# DEFINE - parameter


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet("Ray")
print("result1:", result1)

result2 = greeting("John")
print("result2:", result2)

print("======= KEYWORD & DEFAULT ARGUMENTS ========")
# DEFINE
# def give_greet(name, age):
#     print("give_greet is executed")
#     return f"Hello {name}, you are {age} years old!"


# # CALL
# result3 = give_greet("Justin", 28)
# print("result3:", result3)

# >>>>>>KEYWORD ARGUMENTS<<<<<<<
# DEFINE


# def give_greet(name, age):
#     print("give_greet is executed")
#     return f"Hello {name}, you are {age} years old!"


# # CALL
# result3 = give_greet("Justin", age=28)
# print("result3:", result3)

# >>>>>>DEFAULT ARGUMENTS<<<<<<<
# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hello {name}, you are {age} years old!"


# CALL
result4 = give_greet("Jessica")
print("result4:", result4)
