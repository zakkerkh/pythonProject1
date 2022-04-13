#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#13/04/2022
#Hello, how are you doing

#Question 1a
import random

age = int(input("What is your age?: "))

while age < 16:
    print("You are not old enough")
    age = int(input("What is your age?: "))
print("You are old enough to drive, goodbye!")

#Question 1b
age = int(input("What is your age:"))
while age:
    if age < 0 or age > 130:
        age = int(input("invalid entry, try again: "))
    elif age > 16:
        print("You are old enought to get a lisence")
        quit()
    else:
        age = int(input("You are too young"))

#Question 2a
rand = random.randint(1, 30)
print("the random number is", rand)
print("Enter a number larger than", rand)
entry = int(input())
while entry:
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        quit()

#Question 2a
rand = random.randint(1, 30)
print("the random number is", rand)
print("Enter a number larger than", rand)
entry = int(input())
while entry:
    if entry >= rand+50:
        entry = int(input("Invalid input, try again: "))
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        quit()

#Question 2c
rand = random.randint(1, 30)
print("the random number is", rand)
print("Enter a number larger than", rand)
entry = int(input())
while entry:
    if entry >= rand+50:
        entry = int(input("Invalid input, try again: "))
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        quit()


