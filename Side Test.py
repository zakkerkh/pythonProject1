
import random
name = str.capitalize(input("Enter you name: "))

while name != "End":
    num = random.randint(1, 4)
    if num == 1:
        print("Hello", name + "!")
        name = input("Enter you name: ")
    if num == 2:
        print("Greetings", name + "!")
        name = input("Enter you name: ")
    if num == 3:
        print("Good day", name + "!")
        name = input("Enter you name: ")
    if num == 4:
        print("Hope you are having a fabulous day", name + "!")
        name = input("Enter you name: ")
    name = str.capitalize(name)
    num = random.randint(1, 4)

print("Goodbye! ")