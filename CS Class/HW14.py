#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#20/05/2022
#Hello, how are you doing

#1
# myList = [3, 4, 8, 11, 15]
# count = 0
# num = 0
# repeat = True
#
# while repeat:
#     num1 = input("What number would you like to add to the list?: ")
#     if num1 == "Done":
#         repeat = False
#     else:
#         place = input("Where would you like to add the number?: ")
#
#         myList[int(place)-1] = int(num1)
# print(myList)
# while count != len(myList):
#     count += 1
#     if count % 2 != 0:
#         print("Item", count, "is:", myList[count-1])
#         num += myList[count-1]
#
# myList = [3, 4, 8, 11, 15]
# count = 0
#
# print(num)

#2
Fruits = ["apple", "pear", "peach"]

fruitList = ("The list has the fruits:", Fruits[0].capitalize(), Fruits[1].capitalize(), "and", Fruits[2].capitalize())
veg = []
veg.append(input("Enter a vegatable: "))
veg.append(input("Enter a vegatable: "))
veg.append(input("Enter a vegatable: "))

vegList = ("The list has the vegatables:", veg[0].capitalize(), veg[1].capitalize(), "and", veg[2].capitalize())

food = []
food.append(Fruits)
food.append(veg)

print(food)

print()