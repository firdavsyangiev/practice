import random

x = random.randint(0, 100)
attempt = 0

while True:
    number = int(input("Raqamni toping: "))
    attempt += 1

    if number > x:
        print("Yo'q, lekin kiritgan raqamingizdan kichkina!")

    elif number < x:
        print("Yo'q, lekin kiritgan raqamingizdan katta!")

    else:
        print(f"WOW! Raqam haqiqatda {x}")
        print(f"Siz {attempt} ta urinishda topdingiz!")
        break
