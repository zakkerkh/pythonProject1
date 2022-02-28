#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#28/02/2022
#Hello, how are you doing
import math

radius = float(input("What is the radius of the balloon? (cm): "))
quantity = int(input("How many balloons do you want?: "))
helium_amount = (4*math.pi*radius**3)/3
balloon_amount = 4*math.pi*radius**2
helium_cost = helium_amount*0.75*quantity
balloon_cost = balloon_amount*0.45*quantity

print("Total cost of helium is: $", round(helium_cost, 2))
print("Total cost of the balloon: is $", round(balloon_cost, 2))
print("The subtotal is $:", round(balloon_cost+helium_cost, 2))
print("The total tax is: $", round((balloon_cost+helium_cost)*0.05, 2))
print("The total is: $", round((balloon_cost+helium_cost)*1.05, 2))
