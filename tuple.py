''' Tuple
        (1) What is tuple: tuple va list
        (2) Unpacking arguments
        (3) zip
    '''

print("========= What is tuple: tuple va list ===========")
# Java/PHP/NodeJS array => Python list

# literal
numbs = [3, 5, 1, 2]
#  car_dict = {"brand": "Ferrari", "year": 1995}
#  print(numbs)

# constructor
letter = list("Hello World!")
# print(letter)
#  person_dict = dict(name="Ray", age=25) #dictionary function

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# Tuple >> We can not mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird" #ERROR

# try avoid this
people = "Andrew", "John"
animals = ("dog")  # animals = "dog",


print("========= Unpacking arguments ===========")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, z, a) = groups  # x, y, z, a = groups
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list

# *args > tuple


def calculate(*args):
    print("*args>", args)
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


# call
calculate(1, 7, 2, 3)
print("-------")
calculate(0, 2, 300)
print("-------")
calculate(5, 7)


print("-------")
# **kwargs > dictionary orqali hosil bo'ladi


def introduce(**kwargs):
    print(f"the type (**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


# call
introduce(name="Justin", age=28)
introduce(name="Shawn", age=30, single=True)
print("-------")


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# call
greeting("hi", True, 10, name="John", age=22)
