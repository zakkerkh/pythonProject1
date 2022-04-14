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
    if entry >= 50:
        entry = int(input("Invalid input, try again: "))
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        max = entry
        print("Enter a number greater than", rand, "but less than", max)
        entry = int(input())
        while entry:
            if entry >= 50:
                entry = int(input("Invalid input, try again: "))
            if entry <= rand:
                entry = int(input("Sorry try again"))
            elif max > entry > rand:
                print("goodjob")

#Question 3a
entry = int(input("Enter a number between 0-20"))
while entry:
    if 1 > entry > 20:
        entry = int(input("Enter a number between 0-20"))
    elif 1 < entry < 20:
        print("goodjob")
        quit()

#Question 3b
entry = int(input("Enter a number between 0-20"))
count = 0
times_displayed = 0
while entry:
    if 1 > entry or entry > 20:
        count = count + 1
        entry = int(input("Enter a number between 0-20"))
    elif 1 < entry < 20:
        while count != -1:
            print(1+times_displayed)
            times_displayed = times_displayed + 1
            count = count - 1
        print("Goodjob")
        quit()

#Question 3c
entry = int(input("Enter a number between 0-20: "))
count = 0
times_displayed = 0
org_count = 0
while entry:
    if 1 > entry or entry > 20:
        count = count + 1
        entry = int(input("Enter a number between 0-20: "))
    elif 1 < entry < 20:
        while count != -1:
            print(1+times_displayed)
            org_count = org_count + 1 + times_displayed
            times_displayed = times_displayed + 1
            count = count - 1
        print(org_count)
        print("Goodjob")
        quit()

#Question 3d
entry = int(input("Enter a number between 0-20: "))
count = 0
times_displayed = 0
org_count = 0
while entry:
    if 1 > entry or entry > 20:
        count = count + 1
        entry = int(input("Enter a number between 0-20: "))
    elif 1 < entry < 20:
        while count != -1:
            print(1+times_displayed)
            org_count = org_count + 1 + times_displayed
            times_displayed = times_displayed + 1
            count = count - 1
        print(org_count)
        print("Goodjob")
        quit()



