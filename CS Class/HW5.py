#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#09/03/2022
#Hello, how are you doing

#Planning II
#Question 1

num1 = int(input("What is your first number?: "))
num2 = int(input("What is your second number?: "))

if num1>num2:
    print(num1+num2)
else:
    print(num1*num2)

#Question 4
cloudy = input("is it cloudy?: ")
temp = int(input("What is the temperature?: "))

if temp<0:
    print("Today is cold")
elif temp<25 and cloudy=="yes":
    print("Today is  cloudy")
else:
    print("Today is so warm!!!")

#Question 5
print("Enter your values for A, B, and C with A as the biggest side")
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if A**2==B**2+C**2:
    print("It is a right triangle")
else:
    print("It is not a right triangle")

#Planning I
vacation = input("Are you on vacation?: ")
weekend = input("Is it the weekend?: ")

if vacation=="yes" or weekend=="yes":
    print("You can sleep in")
else:
    print("You cannot sleep in")