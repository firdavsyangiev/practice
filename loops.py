''' LOOP OPERATORS
  (1) for  
  (2) break / else
  (3) while
'''

print("=====for operator=======")
# Iterable objects: string, list, tuple, dict, range, filter, map

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2026)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print("-----")
for num in numbs:
    print(f"the number: {num}")

print("-----")
for x in range_obj:
    print(f"the element: {x}")

print("-----")
for key in car_obj:
    print(f"the key: {key} > value {car_obj.get(key)}")

print("-----")
# for x in range(1, 20, 5):
#     print(f"the x: {x}")


print("=====break and else=======")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("Reached Break")
        break
else:
    print("Looped succesfully")


print("=====while operator=======")
numb = 40

while numb > 0:
    numb -= 10
    print(f"the numb: {numb}")


print("-----")
count = 0
while True:
    count += 1
    x = int(input("Find a number"))

    if x == 41:
        print(f"You found the number in {count} steps!")
        break
    else:
        print("Wrong! Please try again!")
