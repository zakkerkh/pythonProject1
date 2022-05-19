#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#12/05/2022
#Hello, how are you doing
import random

#To force activate the secret level, change line 100 value from 15 to 0 and change line 105 value to 2 instead of the random integer

#greets the users and asks them if they are ready
redo = input("Are you ready? y/n: ")

#this handles invalid inputs
while redo != "y" and redo != "n":
    print("Invalid Input")
    redo = input("Are you ready? y/n: ")

if redo == "y":
    print("Welcome to the Candy Crushinator Game \n")
    print("Made by Zakariyah Khan")
    print("In this game, you will input a string upto 10 characters long. You will then guess what the output will be after all consecutive triplets are removed \n")

#defines all the variables needed for later
list = ""
count = 0
count1 = 0
points = 0
right = "You got it right!"
wrong = "You got it wrong..."
entry1 = ""
complete = False

#this takes the users entry and guess and stores it in 2 places
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
    list = "You entered: " + entry + " Your guess was " + guess

#this is the filtering system which remove all triplets from the user entry and makes multiple passes until all triplets are removed
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
        elif len(entry) >= 8 and entry[5] == entry[6] == entry[7]:
            entry = entry[0:5] + entry[8:]
            count1 += 1
        elif len(entry) >= 9 and entry[6] == entry[7] == entry[8]:
            entry = entry[0:6] + entry[9:]
            count1 += 1
        elif len(entry) >= 10 and entry[7] == entry[8] == entry[9]:
            entry = entry[0:7] + entry[10:]
            count1 += 1
        count += 1

    #this stores the correct answer with the users entry to display in final results
    print(entry)
    list += ". The answer is: " + entry + ". "

    if guess == entry:
        print("\n" + right + "\n")
        list += right + "|||"
        points += 1
    else:
        print("\n" + wrong + "\n")
        list += wrong + "|||"

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

#this displays the final points and results
final = "Final results: " + list
if len(final) != 15:
    print(final)
    print("Your final score is:", points)

#this has a random chance of activating the secret level and starts the AI character
    num = random.randint(1, 3)
    if num == 2:
        entry = ""
        print("SECRET LEVEL \n")
        print("**booting**")
        print("**initializing**\n")
        print("AI: I've immerged")
        print("AI: You are one of the few to unlock the true power of the Candy Crushinator game...")
        print("AI: Are you ready for the challenge?")
        hard = input("AI: Would you like to unlock the secret level? y/n: ")
        #this deals with invalid inputs
        while hard != "y" and hard != "n":
            print("invalid Input")
            hard = input("AI: Would you like to unlock the secret level? y/n: ")
        if hard == "n":
            print("AI: It seems as though you are not up to the challenge, but do not feel ashamed as most are not fit")
        if hard == "y":
            print("\nAI: I am surprised, you are brave now. Let's see how you are later. My friends Siri, Alexa and Google Assistant are watching you with NFT popcorn.")
            print("With this level the characters are unlimited and you have to remove quadruplets and quintuplets\n")
            hard = input("AI: Are you still sure that you want to play? y/n: ")
        while hard != "y" and hard != "n":
            print("invalid Input")
            hard = input("AI: Are you still sure that you want to play? y/n: ")
        #this ends the while loop if they select no
        if hard == "n":
            print("AI: I thought so")
            print("AI: **power down**")
        #this takes the users entry
        if hard == "y":
            entry = input("Enter your daring string: ")
            guess = input("What is you guess: ")

        if len(entry) < 15 and len(entry) > 0:
            print("\nI see you are going the easy route")

        #this is the universal filtering system which removes all quadruplets including the ones generated by removing quadruplets
        while hard == "y" and not complete:
            list += "You entered: " + entry + " --- Your guess was: " + guess + " ---"

            entry1 = entry
            entry = entry.replace("aaaa", "")
            entry = entry.replace("bbbb", "")
            entry = entry.replace("cccc", "")
            entry = entry.replace("dddd", "")
            entry = entry.replace("eeee", "")
            entry = entry.replace("ffff", "")
            entry = entry.replace("gggg", "")
            entry = entry.replace("hhhh", "")
            entry = entry.replace("iiii", "")
            entry = entry.replace("jjjj", "")
            entry = entry.replace("kkkk", "")
            entry = entry.replace("llll", "")
            entry = entry.replace("mmmm", "")
            entry = entry.replace("nnnn", "")
            entry = entry.replace("oooo", "")
            entry = entry.replace("pppp", "")
            entry = entry.replace("qqqq", "")
            entry = entry.replace("rrrr", "")
            entry = entry.replace("ssss", "")
            entry = entry.replace("tttt", "")
            entry = entry.replace("uuuu", "")
            entry = entry.replace("vvvv", "")
            entry = entry.replace("wwww", "")
            entry = entry.replace("xxxx", "")
            entry = entry.replace("yyyy", "")
            entry = entry.replace("zzzz", "")
            entry = entry.replace("aaaaa", "")
            entry = entry.replace("bbbbb", "")
            entry = entry.replace("ccccc", "")
            entry = entry.replace("ddddd", "")
            entry = entry.replace("eeeee", "")
            entry = entry.replace("fffff", "")
            entry = entry.replace("ggggg", "")
            entry = entry.replace("hhhhh", "")
            entry = entry.replace("iiiii", "")
            entry = entry.replace("jjjjj", "")
            entry = entry.replace("kkkkk", "")
            entry = entry.replace("lllll", "")
            entry = entry.replace("mmmmm", "")
            entry = entry.replace("nnnnn", "")
            entry = entry.replace("ooooo", "")
            entry = entry.replace("ppppp", "")
            entry = entry.replace("qqqqq", "")
            entry = entry.replace("rrrrr", "")
            entry = entry.replace("sssss", "")
            entry = entry.replace("ttttt", "")
            entry = entry.replace("uuuuu", "")
            entry = entry.replace("vvvvv", "")
            entry = entry.replace("wwwww", "")
            entry = entry.replace("xxxxx", "")
            entry = entry.replace("yyyyy", "")
            entry = entry.replace("zzzzz", "")

            #this adds the users entry, guess and the answer to a single variable to display later
            if entry1 == entry:
                complete = True
            if complete:
                if guess == entry:
                    print(right)
                    points += 2
                    list += " " + right +"|||"
                else:
                    print(wrong)
                    print("AI: Hahahaha")
                    list += " " + wrong + "|||"
                if len(entry) == 0:
                    print("(Blank)")
                #this asks if the user wants to play again and deals with invalid inputs
                else:
                    print("\nThe correct answer is: " + entry)
                hard = input("Do you dare to play again? y/n:")
                while hard != "y" and hard != "n":
                    print("Invalid Input")
                    hard = input("Do you dare to play again? y/n:")
                if hard == "n":
                    complete = True
                    print("Very well")
                    print("**shut down**\n")
                if hard == "y":
                    complete = False
                    entry = input("Enter your daring string: ")
                    guess = input("What is you guess: ")
                    if len(entry) < 15 and len(entry) > 0:
                        print("I see you are going the easy route")

#displays final results, points and greets the player
print(list)
print("You final score after the secret level is:", points)
print("\nThank you for running the Candy Crushinator")
print("Goodbye")