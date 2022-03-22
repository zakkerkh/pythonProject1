#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#09/03/2022
#Hello, how are you doing
import random
import math

#Round Numbers I
#Question 1
var1 = random.randint(0, 20)
var2 = random.randint(0, 20)
var3 = random.randint(0, 20)
var4 = random.randint(0, 20)
var5 = random.randint(0, 20)
print((var5+var4+var3+var2+var1)/5)

#Question 2
sphere = round(random.uniform(5, 10), 1)
cube = round(random.uniform(5, 10), 1)
rectangulLength = round(random.uniform(5,10), 1)
rectangulWidth = round(random.uniform(5,10), 1)
rectangulHeight = round(random.uniform(5,10), 1)
spheretotal = (2/3)*math.pi*sphere
print("Sphere height is:", round(spheretotal, 1))
print("Cube height is:", round(cube**3, 1))
print("Rectangular prism height is:", round(rectangulHeight*rectangulWidth*rectangulLength, 1))

#Question 3
variable1 = random.randint(10, 30)
variable2 = random.randint(variable1, 30)
print("Your random numbers are,", variable1, "and", variable2)

#Random Numbers II
#Question 1
value1 = int(input("Enter First Number"))
value2 = int(input("Enter Second Number"))
random_value = random.randint(value1, value2)
print(value1, random_value, value2)

#Question 2
num1 = random.randint(-5, 8)
num2 = random.randint(-5, 8)
print("Addition:", num1, "+", num2, "=", num1+num2)
print("Subtraction:", num1, "-", num2, "=", num1-num2)
print("Multiplication:", num1, "*", num2, "=", num1*num2)
print("Exponents:", num1, "^", num2, "=", num1**num2)
print("Integer Division:", num1, "//", num2, "=", num1//num2)
print("Modulus:", num1, "%", num2, "=", num1%num2)

#Question 3
age1 = int(input("What is your age? "))
random_year = random.randint(age1, 120)-age1+2022
random_age = random_year-(2022-age1)
print("You were born in", 2022-age1, "in", random_year, "you will be", random_age)

#Random Numbers III
#Question 1

x1 = random.randint(-10, 10)
x2 = random.randint(-10, 10)
y1 = random.randint(-10, 10)
y2 = random.randint(-10, 10)

print("Point 1:", x1, ",", y1)
print("Point 2:", x2, ",", y2)

midpoint_x = (x1+x2)/2
midpoint_y = (y1+y2)/2
print("The midpoint between the 2 points are:", midpoint_x, ",", midpoint_y)

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("The distance between the points is:", distance)

#Question 2
x3 = (random.randrange(-10, 10, 2))+1
x4 = (random.randrange(-10, 10, 2))+1
y3 = (random.randrange(-10, 10, 2))+1
y4 = (random.randrange(-10, 10, 2))+1

print("Point 1:", x3, ",", y3)
print("Point 2:", x4, ",", y4)

slope = ((y3-y4)/(x3-x4))
b = slope*x3-y4
print("The equation of the line is: y =", slope, "x +", b)

#Question 3
slope1 = random.randrange(0, 50, 2)
y_int = random.randrange(0, 50, 2)

point_x1 = random.randint(1, 50)
point_y1 = slope1*point_x1+y_int
point1 = point_x1, point_y1

point_x2 = random.randint(1, 50)
point_y2 = slope1*point_x2+y_int
point2 = point_x2, point_y2

point_x3 = random.randint(1, 50)
point_y3 = slope1*point_x3+y_int
point3 = point_x3, point_y3

print("On the equation of a line with a y intercept of", y_int, "and a slope of", slope1, "Three points that lay on this line are:\n", point1, "\n", point2, "\n", point3)