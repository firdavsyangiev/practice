'''CLASS
   (1) What is a class?
   (2) Ordinary and static properties
   (3) Special/magic methods
'''

print("=====What is a class?=======")
# class: blueprint for object creation!
# Structure > state constructor method


class Person():
    # state
    message = "static state property"
    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method

    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says I am {self.age}")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Ray", 24)
person2 = Person("Martin", 35)
person3 = Person("John", 25)

# ordinary state
print("person1 name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("=====Ordinary and static properties=======")
# static state property
new_message = Person.message
print("Static message:", new_message)

# static method property
Person.explain()


print("=====Special/magic methods=======")
# Pthon's most common special methods are below:
# --init__ __new__ __str__  __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = "This class makes cars"

# constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

# method
    def start_engine(self):
        print(f"{self.name} started engine!")

    def stop_engine(self):
        print(f"{self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year."

    def __call__(self):
        print("Object called as function!")
        return True


my_car = Car("Ferrari", 2026)
my_car.start_engine()
my_car.stop_engine()

print("--------")
your_car = Car("Toyota", 2026)
print(your_car)
your_car()  # CALL
response = your_car()
print("Response:", response)
