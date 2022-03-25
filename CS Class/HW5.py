#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#09/03/2022
#Hello, how are you doing

#Planning II
#Question 1
import random

num1 = int(input("What is your first number?: "))
num2 = int(input("What is your second number?: "))

if num1 > num2:
    print(num1+num2)
else:
    print(num1*num2)

#Question 4
cloudy = input("is it cloudy?: ")
temp = int(input("What is the temperature? y/n: "))

if temp < 0:
    print("Today is cold")
elif temp < 25 and cloudy == "y":
    print("Today is  cloudy")
else:
    print("Today is so warm!!!")

#Question 5
print("Enter your values for A, B, and C with A as the biggest side")
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if A**2 == B**2+C**2:
    print("It is a right triangle")
else:
    print("It is not a right triangle")

#Planning I
#Question 2
vacation = input("Are you on vacation? y/n: ")
weekend = input("Is it the weekend? y/n: ")

if vacation == "y" or weekend == "y":
    print("You can sleep in")
else:
    print("You cannot sleep in")

#Question 3


score = 0

def game(score):
    number = random.randint(10, 15)
    guess = int(input("Guess a number between 10 and 15: "))

    if guess == number:
        score = score+3
        print("You got it")
        print(score)
    else:
        score = score-1
        print(score)
        print("Try again")
    play = input("Would you like to play again y/n?: ")
    if play == "y":
        game(score)
    else:
        print("Thank you for playing")
        quit()
game(score)

