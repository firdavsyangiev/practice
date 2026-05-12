'''CLASS
   (1) What is a class?
   (2) Ordinary and static properties
   (3) Special methods
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
