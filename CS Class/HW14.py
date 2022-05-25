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
# Fruits = ["apple", "pear", "peach"]
#
# fruitList = ("The list has the fruits:", Fruits[0].capitalize(), Fruits[1].capitalize(), "and", Fruits[2].capitalize())
# veg = []
# veg.append(input("Enter a vegatable: "))
# veg.append(input("Enter a vegatable: "))
# veg.append(input("Enter a vegatable: "))
#
# vegList = ("The list has the vegatables:", veg[0].capitalize(), veg[1].capitalize(), "and", veg[2].capitalize())
#
# food = []
# food.append(Fruits)
# food.append(veg)
#
# food2 = food
# #print(food[0][1].replace("a", "-"))
# food[0][0] = food[0][0].replace("a", "-")
# food[0][1] = food[0][1].replace("a", "-")
# food[0][2] = food[0][2].replace("a", "-")
# food[1][0] = food[1][0].replace("a", "-")
# food[1][1] = food[1][1].replace("a", "-")
# food[1][2] = food[1][2].replace("a", "-")
#
# food[0][0] = food[0][0].replace("e", "-")
# food[0][1] = food[0][1].replace("e", "-")
# food[0][2] = food[0][2].replace("e", "-")
# food[1][0] = food[1][0].replace("e", "-")
# food[1][1] = food[1][1].replace("e", "-")
# food[1][2] = food[1][2].replace("e", "-")
#
# food[0][0] = food[0][0].replace("i", "-")
# food[0][1] = food[0][1].replace("i", "-")
# food[0][2] = food[0][2].replace("i", "-")
# food[1][0] = food[1][0].replace("i", "-")
# food[1][1] = food[1][1].replace("i", "-")
# food[1][2] = food[1][2].replace("i", "-")
#
# food[0][0] = food[0][0].replace("o", "-")
# food[0][1] = food[0][1].replace("o", "-")
# food[0][2] = food[0][2].replace("o", "-")
# food[1][0] = food[1][0].replace("o", "-")
# food[1][1] = food[1][1].replace("o", "-")
# food[1][2] = food[1][2].replace("o", "-")
#
# food[0][0] = food[0][0].replace("u", "-")
# food[0][1] = food[0][1].replace("u", "-")
# food[0][2] = food[0][2].replace("u", "-")
# food[1][0] = food[1][0].replace("u", "-")
# food[1][1] = food[1][1].replace("u", "-")
# food[1][2] = food[1][2].replace("u", "-")
#
# print(food)
# food = food2
# food.append(Fruits[0])
# food.append(Fruits[1])
# food.append(Fruits[2])
# food.append(veg[0])
# food.append(veg[1])
# food.append(veg[2])
#
# count = 0
#
# length = (len(food))
# while count != length:
# #    food1 = food[count]
#     if not (food[count].startswith("a") or food[count].startswith("e") or food[count].startswith("i") or food[count].startswith("o") or food[count].startswith("u")):
#         print(food)
#     count += 1

#3
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# num4 = int(input("Enter a number: "))
#
# list = [num1, num2, num3, num4]
# count = 0
#
# while count != 4:
#     list[count] += 3
#     count += 1
#
# print(list)
#
# add = int(input("Enter a positive number: "))
#
# count = 0
#
# while count != 4:
#     list[count] += add
#     count += 1
#
# print(list)
#
# add = int(input("Enter a negative number: "))
#
# count = 0
#
# while count != 4:
#     list[count] += add
#     count += 1
#
# print(list)

#4
# list = [int(input("Enter a number: ")), int(input("Enter a number: "))]
# if list[0] > list[1]:
#     print("True")
# else:
#     print("False")
#     list = [list[1], list[0]]
# print(list)

list = [int(input("Enter a number: ")), int(input("Enter a number: ")), int(input("Enter a number: "))]

list.sort(reverse=True)
print(list)