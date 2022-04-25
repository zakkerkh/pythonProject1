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

#Strings II
#1a
word1 = input("Enter 1st word") #takes first word
word2 = input("Enter 2nd word") #takes second word

print(word1, "!=", word2) #prints both words with not equals symbol

#1b
word1 = input("Enter 1st word")  # takes first word
word2 = input("Enter 2nd word")  # takes second word

while word1 != word2: #checks if they 2 entrys are not equal
    print(word1, "!=", word2)  # prints both words with not equals symbol

    word1 = input("Enter 1st word")  # takes first word
    word2 = input("Enter 2nd word")  # takes second word

print(word1, "==", word2) #if the entries are equal it tells the user than it says goodbye
print("Goodbye")

#1c
word1 = input("Enter 1st word")  # takes first word
word2 = input("Enter 2nd word")  # takes second word

while word1 != word2:
    print("if", word1, "!=", word2 + ":") #these four lines print the if statement
    print("      print(\"Play again\")")
    print("else" + ":")
    print("      print(\"Goodbye! \")")

    word1 = input("Enter 1st word")  # takes first word
    word2 = input("Enter 2nd word")  # takes second word

print(word1, "==", word2) #if the entries are equal it tells the user than it says goodbye
print("Goodbye")

#2
word1 = input("First word") #asks user for their words
word2 = input("Second word")

while word1 != "end" and ((len(word1) > 1 or len(word2) > 1)): #Checks if the string is one charcter or if the user wants to end
    word1 = word1[1:] #removes the first character
    word2 = word2[1:]
    word3 = str.capitalize(word1 + word2) #Capitalizes it
    print(word3) #prints it
    word1 = input("First word") #Asks again for the words
    word2 = input("Second word")

print("goodbye")

#3
word1 = input("Enter a words 4 at least 4 characters long: ")

while word1 != "end":
    print(str.capitalize(word1[2: 5] + word1[0:2] + word1[5:]))
    word1 = input("Enter a words 4 at least 4 characters long: ")

print("Goodbye")



