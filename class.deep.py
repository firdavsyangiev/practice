'''CLASS DEEP DIVING
   (1) Inheritance
   (2) Encapsulation
   (3) Polymorphism     
'''

print("=====Encapsulation=======")
# Python > public, __private, _protected


class Accaunt():
    # state
    description = "This class makes account"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount  # private state property

    # method
    def get_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("Deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("Withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("Changing ownership:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("Changing ownership:", new_owner)
        self.__owner = new_owner


my_accaunt = Accaunt("Ray", 1000)
my_accaunt.get_balance()

print("============")
my_accaunt.deposit(3500)
my_accaunt.withdraw(400)
my_accaunt.get_balance()

# print("============")
# my_accaunt.amount = 1000000
# my_accaunt.owner = "Martin"
# my_accaunt.amount = 10000000
# my_accaunt.owner = "Martin"
# my_accaunt.get_balance()

print("============")
# print(my_accaunt.__owner)  # ERROR

try:
    result = my_accaunt.__amount
    print("Result:", result)
except Exception as err:
    print("No target state found", err)

# accaunt_owner = my_accaunt.holder
# print("Accaunt owner:", accaunt_owner)

# print("=====Getter=====")
# print("Owner before:", my_accaunt.holder)
# my_accaunt.change_ownership("Martin")
# print("Owner after:", my_accaunt.holder)


print("=====Setter=====")
print("Owner before:", my_accaunt.holder)
my_accaunt.holder = "Martin"
print("Owner after:", my_accaunt.holder)
