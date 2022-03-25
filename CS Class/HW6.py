import random
#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#25/03/2022
#Hello, how are you doing

#Question 1
mark = int(input("What is your grade?: "))

if mark > 100 or mark < 0:
    print("Invalid entry")
elif mark > 90:
    print("You are doing an excellent job!")
elif mark > 80:
    print("Work harder and you can do better")
elif mark > 50:
    print("You are passing")
elif mark > 0:
    print("You are failing")

#Question 2
num = int(input("What is the number?: "))

if num < 0:
    print("It is a negative number")
elif num == 0:
    print("Your number is neither positive or negative")
else:
    print("Your number is positive")

#Question 3
num1 = int(input("What is the number?:"))

if num1%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

#Question 4
print("Package Calculator")
numb1 = int(input("Length: "))
numb2 = int(input("Width: "))
numb3 = int(input("Height: "))

if numb1*numb2*numb3 <= 0:
    print("Invalid entry")
elif numb1*numb2*numb3 < 1000:
    print("Your package is acceptable")
else:
    print("Package is too large")

#Question 5
rand_numb = random.randint(-5, 10)

if rand_numb < 0:
    print("The number is negative")
elif 0 <= rand_numb <= 4:
    print(rand_numb)
else:
    print("The number is too large")

#Question 6
age = int(input("What is your age?: "))

if age <= 0:
    print("Invalid entry")
elif age < 3:
    print("Toddler")
elif age < 10:
    print("Child")
elif age < 12:
    print("Preteen")
elif age < 18:
    print("Teen")
else:
    print("Adult")