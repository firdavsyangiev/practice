'''CLASS DEEP DIVING
   (1) Encapsulation
   (2) Inheritance <
   (3) Polymorphism  <   
'''

print("=====Inheritance=======")


class Animal():
    # state
    description = "This class is Parent for animals"
    # constructor

    def __init__(self, voice):
        self._status = "This animal is alive!"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"The animal can makevoice: {self.voice}")


class Dog(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"{self.name} says {self.sound}")


class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "woof-woof", True)
cat = Cat("Tom", "meow-meow", True)
fish = Fish("Bubbles", "Zzzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("============")
dog.make_voice()
cat.make_voice()

print("============")
print(Animal.description)
print(dog.description)

print("============")
print(dog._status)
print(cat._status)


print("=====Polymorphism=======")
dog.make_voice()
cat.make_voice()

print("============")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"Result: {result}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
