#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#26/05/2022
#Hello, how are you doing

#1a
# list = [input("Enter a name: "), input("Enter a name: "), input("Enter a name: "), input("Enter a name: "), input("Enter a name: "),]
# list.sort()
# print(list)

#b
# list = []
# repeat = True
# while repeat:
#     entry = input("Enter a name: ")
#     if entry == "done":
#         repeat = False
#     list.append(entry)
# list.sort()
# print(list)

#c
# list = []
# list1 = []
# list2 = ["a","b","c","d","e","f", "g", "h", "i", "j", "k", "l", "m"]
# repeat = True
# while repeat:
#     entry = input("Enter a name: ")
#     if entry == "done":
#         repeat = False
#     if entry != "done":
#         if entry[0] in list2:
#             list.append(entry)
#         else:
#             list1.append(entry)
# list.sort()
# list1.sort()
# print(list)
# print(list1)

#2a
# list = []
# count = 3
# while count != 0:
#     list.append(int(input("Enter a number: ")))
#     count -= 1
#
# entry = int(input("Enter another number: "))
# if entry in list:
#     position = list.index(entry)
#     list.insert(position, 0)
#     list.remove(position+1)
#
# print(list)

#3a/b
# import random
#
# myList = ["Computer", "Malware", "Software", "Technology"]
# guess = input("What is your guess?: ")
#
# if guess in myList:
#     print("You got it correct")
#
# num = random.randint(0, 3)
# secret = myList[num]
# myList.remove(myList[num])
# print(myList)
#
# correct = False
# while not correct:
#     guess = input("What is your guess?: ")
#     if guess == secret:
#         print("You guessed the secret word")
#         correct = True
#     else:
#         print("You got it wrong")

#Even More List Practice
import random

#1
# list = []
# num = random.randint(1,2)
# if num == 1:
#     count = 5
#     while count != 0:
#         count -= 1
#         list.append(random.randint(10, 20))
# else:
#     count = 10
#     while count != 0:
#         count -= 1
#         list.append(random.randint(10, 20))
# print(num)
# print(list)
#
# if list[1] == 15 or list[-2] == 15:
#     print("True")
# else:
#     print("False")

#2
# num = int(input("Enter a number between 10 an 20"))
# num1 = int(input("Enter a number between 10 an 20"))
# list = []
# list1 = []
#
# if num > num1:
#     count = 100
# #    count1 = 0
#     while count-100 != num:
#         list.append(1+count)
#         if count-100 != num1:
#             list1.append(1+count/num1)
#         count += 1
#
# if num < num1:
#     count = 100
#     count1 = 0
#     while count-100 != num1:
#         list.append(1+count)
#         if count1 != num:
#             list1.append(1+count/num)
#             count1 += 1
#         count += 1
#
# print(list)
# print(list1)

#3
# num = int(input("Enter a number between 1 and 5: "))
# num1 = int(input("Enter a number between 1 and 5: "))
#
# list = []
# list1 = []
#
# while len(list) != num:
#     var = random.randint(10, 20)
#     list.append(var)
#
# while len(list1) != num1:
#     var = random.randint(10, 20)
#     list.append(var)
#
# if list[0] == list1[0] or list[-1] == list1[-1]:
#     print("Bingo")
# else:
#     print("False")

#4
# count = 5
# list = []
# while count != 0:
#     list.append(input("Enter a word: "))
#     count -= 1
#
# num = int(input("Enter a number: "))
#
# while count != 5:
#     if len(list[count]) == num:
#         print(list[count])
#     count += 1

#coding practice
#J1
# list = []
# w_count = 0
# l_count = 0
# count = 0
# group = 0
#
# while count != 6:
#     entry = input("Enter W or L: ")
#     if entry == "W":
#         w_count += 1
#     else:
#         l_count += 1
#     count += 1
#
# if w_count >= 5:
#     print("1")
# elif w_count >= 3:
#     print("2")
# elif w_count >= 1:
#     print("3")
# else:
#     print("-1, Fatality")

#J2
