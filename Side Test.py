import math
import random
#Question 3
#MAKE SURE IT IS EVEN
slope1 = random.randint(1, 50)
y_int = random.randint(1, 50)

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

