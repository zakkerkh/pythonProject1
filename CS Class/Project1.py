#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#12/05/2022
#Hello, how are you doing
import random

print("Welcome to the Candy Crushinator Game \n")
print("Made by Zakariyah Khan")
print("In this game, you will inpute a string upto 10 characters long. You will then guess what the output will be after all consecutive triplets are removed \n")
redo = input("Are you ready? y/n: ")

while redo != "y" or redo != "n":
    print("invalid Inputtttt")
    redo = input("Are you ready? y/n: ")
list = ""
count = 0
count1 = 0
points = 0

if redo == "y":
    entry = input("Enter a string up to 10 characters long: ")
    while len(entry) > 10:
        print("Invalid Input: Entry has a limit of 10 characters")
        entry = input("Enter a string up to 10 characters long: ")
    guess = input("What is you guess: ")
    count = 0
    count1 = 0
    points = 0
    redo = "y"
    list = "You entered: " + entry

    right = " You got it right!"
    wrong = " You got it wrong..."

while redo == "y":
    while count < 10:
        if len(entry) >= 3 and entry[0] == entry[1] == entry[2]:
            entry = entry[3:]
            count1 += 1
        elif len(entry) >= 4 and entry[1] == entry[2] == entry[3]:
            entry = entry[0:1] + entry[4:]
            count1 += 1
        elif len(entry) >= 5 and entry[2] == entry[3] == entry[4]:
            entry = entry[0:2] + entry[5:]
            count1 += 1
        elif len(entry) >= 6 and entry[3] == entry[4] == entry[5]:
            entry = entry[0:3] + entry[6:]
            count1 += 1
        elif len(entry) >= 7 and entry[4] == entry[5] == entry[6]:
            entry = entry[0:4] + entry[7:]
            count1 += 1
        elif len(entry) >= 8 and entry[5] == entry[6] == entry[7]: #Start here
            entry = entry[0:5] + entry[8:]
            count1 += 1
        elif len(entry) >= 9 and entry[6] == entry[7] == entry[8]:
            entry = entry[0:6] + entry[9:]
            count1 += 1
        elif len(entry) >= 10 and entry[7] == entry[8] == entry[9]:
            entry = entry[0:7] + entry[10:]
            count1 += 1
        count += 1

    print(entry)
    list = list + " the answer is " + entry + " "

    if guess == entry:
        print("\n" + right + "\n")
        list += " " + right + "|"
        points += 1
    else:
        print("\n" + wrong + "\n")
        list += wrong + "|"

    redo = input("Would you like to play again? y/n: ")
    if redo == "y":
        entry = input("Enter a string up to 10 characters long: ")
        while len(entry) > 10:
            print("Invalid Input: Entry has a limit of 10 characters")
            entry = input("Enter a string up to 10 characters long: ")
        guess = input("Your guess?: ")
        count = 0
        count1 = 0
        list += "You entered: " + entry + ":"

final = "Final results: " + list
if len(final) != 15:
    print(final)
    print("Your final score is:", points)

    num = random.randint(1, 3)
    if num == 2:
        print("Secret level \n")
        print("**booting**")
        print(random.randint(10 * 99 ** 10000000, 10 * 99 ** 10000001))
        print("AI: **initializing**")
        print("AI: I've immerged")
        print("AI: You are one of the few to unlock the true power of the Candy Crushinator game...")
        print("AI: Are you ready for the challenge?")
        hard = input("AI: Would you like to unlock the secret level? y/n: ")
        while hard != ("y" or "n"):
            print("invalid Input")
            hard = input("AI: Would you like to unlock the secret level? y/n: ")
        if hard == "n":
            print("AI: It seems as though you are not up to the challenge, but do not feel ashamed as most are not fit")
        if hard == "y":
            print("AI: I am surprised, you are brave now. Let's see how you are later. My friends Siri, Alexa and Google Assistant are watching you with NFT popcorn.")
            print("With this level the characters are unlimited and you have to remove quadruplets")
            hard = input("AI: Are you still sure that you want to play? y/n: ")
        while hard != ("y" or "n"):
            print("invalid Input")
            hard = input("AI: Are you still sure that you want to play? y/n: ")
        if hard == "n":
            print("AI: I thought so")
            print("AI: **power down**")


print("Thank you for running the Candy Crushinator")
print("Goodbye")