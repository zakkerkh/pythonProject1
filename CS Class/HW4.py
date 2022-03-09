#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#09/03/2022
#Hello, how are you doing
import random
import math

var1 = random.randint(0, 20)
var2 = random.randint(0, 20)
var3 = random.randint(0, 20)
var4 = random.randint(0, 20)
var5 = random.randint(0, 20)
print((var5+var4+var3+var2+var1)/5)

sphere = random.randint(5, 10)
cube = random.randint(5, 10)
rectangulLength =random.randint(5,10)
rectangulWidth =random.randint(5,10)
rectangulHeight =random.randint(5,10)
spheretotal = (2/3)*math.pi*sphere
print("Sphere height is:", round(spheretotal, 1))
print("Cube height is:", cube**3)
print("Rectangular prism height is:", rectangulHeight*rectangulWidth*rectangulLength)


