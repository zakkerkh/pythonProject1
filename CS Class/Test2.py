#Zakariyah. M. J. Khan & Amir S
#ICS2O_2122_S2
#30/03/2022
#Hello, how are you doing
import random

#This tells the user what the game is about
print("Random number game")
print("You'll have to guess a number between 100 and 150")
print("You can get a hint if you'd like but you'll lose 20% of your points if you get it right")

#This sets the answer to the game
answer = random.randint(100, 150)
#This sets the starting score of 0
score = 0
#This asks if the users wants a hint
hint = input("Would you like a hint? y/n?: ")

#This if structure executes and outputs based on the user's answer
if hint=="y":
    print("The number is above", answer-random.randint(10, 15), "but below", answer+random.randint(10, 15))
elif hint != "y" and hint !="n":
    print("Invalid Entry")

#This asks the user for their answer
user_answer = int(input("What is your guess?: "))

#This if structure is what the program displays depending on if they get is right or not
if user_answer==answer:
    print("You got it right!") #When they get it right
    score = score+100
elif user_answer==answer+1 or user_answer==answer-1:
    print("You got it wrong") #When they were 1 off
    print("You were 1 off")
elif user_answer==answer+5 or user_answer==answer-5:
    print("You got it wrong") #When they were 5 off
    print("You were 5 off")
elif user_answer==answer+10 or user_answer==answer-10:
    print("You got it wrong") #When they were 10 off
    print("You were 10 off")
elif user_answer==answer+15 or user_answer==answer-15:
    print("You got it wrong") #When they were 15 off
    print("You were 15 off")
else:
    print("You got it wrong, You were far off")

#This determines their scores based on if they got it right and if they wanted the hint
if hint=="y":
    score==score-(0.2*score)

#This prints the score
print("Your score is: ", score, "/ 100")



