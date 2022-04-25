#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#25/04/2022
#Hello, how are you doing

#1a
import random

word1 = input("Enter word")
word2 = input("Enter word")

print(word1, word2, word2, word1)

#1b
word1 = input("Enter word")
word2 = input("Enter word")

print(word1, word2, word2, word1)

yes= input("Enter more words? y/n")
while yes == "y":
    word1 = input("Enter word")
    word2 = input("Enter word")

    print(word1, word2, word2, word1)
    yes = input("Enter more words? y/n")
if yes == "n":
    print("goodbye")

#2a/b
play = input("Would you like to play: y/n ")

word1 = ""
while word1 != "end" and play == "y":
    word1 = input("Enter a word: ")
    html = input("Enter a format: bold/italics/underline ")

    if html == "italics":
        print("<i>" + word1 + "</i>")
    elif html == "bold":
        print("<b>" + word1 + "</b>")
    elif html == "underline":
        print("<u>" + word1 + "</u>")

    word1 = input("Enter a word: ")

print("Goodbye")

#2ba
name = input("Enter you name: ")
while name != "end":
    print("Hello", name + "!")
    name = input("Enter you name: ")

print("Goodbye! ")

# 2bb/bc
import random
name = input("Enter you name: ")

while name != "end":
    num = random.randint(1, 4)
    if num == 1:
        print("Hello", name + "!")
        name = input("Enter you name: ")
    if num == 2:
        print("Greetings", name + "!")
        name = input("Enter you name: ")
    if num == 3:
        print("Good day", name + "!")
        name = input("Enter you name: ")
    if num == 4:
        print("Hope you are having a fabulous day", name + "!")
        name = input("Enter you name: ")
    num = random.randint(1, 4)

print("Goodbye! ")

#2d
name = str.capitalize(input("Enter you name: "))

while name != "End":
    num = random.randint(1, 4)
    if num == 1:
        print("Hello", name + "!")
        name = input("Enter you name: ")
    if num == 2:
        print("Greetings", name + "!")
        name = input("Enter you name: ")
    if num == 3:
        print("Good day", name + "!")
        name = input("Enter you name: ")
    if num == 4:
        print("Hope you are having a fabulous day", name + "!")
        name = input("Enter you name: ")
    name = str.capitalize(name)
    num = random.randint(1, 4)

print("Goodbye! ")