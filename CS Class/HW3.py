#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#25/02/2022
#Hello, how are you doing

import math
#how you are not supposed to do it
#name = print("Enter your name")
#print ("hello" name!)
#print ("each apple costs 0.78 cents")
#apples = input("Enter the number of apples you wish to buy")
#apples * 0.78 = cost
#input("Your total cost", cost)

#Question 1
#How you are supposed to do it
name = input("Enter your name ")
print("Hello", name, "!") #You can use "+" instead of the second comma to eliminate to space

print("Each apple costs 0.78 dollars")
apples = int(input("How much do you wish to buy "))
apple_cost = apples * 0.78 * 1.13
print("Your apple cost is", apple_cost)

print("Each orange costs 0.64 dollars")
oranges = int(input("How much do you wish to buy "))
orange_cost = oranges * 0.64 * 1.13
print("Your orange cost is", orange_cost)

print("Each banana costs 1.21 dollars")
bananas = int(input("How much do you wish to buy "))
banana_cost = bananas * 1.21 * 1.13
print("Your banana cost is", banana_cost)
print("Your total cost is:", banana_cost+orange_cost+apple_cost)


# Question 2
# He gets the wrong answer since using the "//" which gives you integer divison which alters the number since there are no tenths places and smaller
print(8/9+3/2)

#Question 3
name = input("What is your name?: ")
age = int(input("What is your age?: "))
print(name, ", you were born in", 2022-age)

#Question 4
print("Evaluating (1/4)x^2 + 4xy - 7xy^3")
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
print("Evaluating (1/4)", x, "^ 2", "+ 4 *", x, "*", y, "-7", "*", x, "*", y, "^ 3")
print("The value is:", (1/4) * x**2 + 4 * x * y - 7 * x * y**3)

#Question 5
#Wrong version
#print("Welcome to a "program" :)")
#Int(Input("What is your" age?)
#Print(age is a wonderful age!)

#Correct Version
print("Welcome to a program :)")
age = int(input("What is your age? ")
print(age, "is a wonderful age!")


#Question 5

