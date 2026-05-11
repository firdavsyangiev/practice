print("=====Iterable objects and RANGE=======")
# Iterable objects: string, list, tuple, dict, range, filter, map

range_obj = range(3)
print(f"Range object: {range_obj}")

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")

print("=====DICTIONARIES=======")
# Dictionaries is JSON object!
person = {"name": "Ray", "age": 30, "single": True}
person_obj = dict(name="Ray", age=30, single=True)
print(f"Person: {person}")
print(f"Person object: {person_obj}")

name = person_obj["name"]
print(f"Name: {name}")

# name2 = person_obj["hobby"]
# print(f"Name2: {name2}")

# method: get()
name2 = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name2: {name2}, hobby: {hobby}, balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} > value {person_obj.get(key)}")
