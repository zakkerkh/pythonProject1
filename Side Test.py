import random
#Question 3

number = random.randint(10, 15)
print(number)
guess = int(input("Guess a number between 10 and 15: "))
score = 0

def game(score, guess):

    if guess==number:
        score = score+3
        print("You got it")
        print(score)
    else:
        score = score-1
        print("Try again")
        print(score)
    play = input("Would you like to play again y/n?: ")
    if play=="y":
        guess = int(input("Guess a number between 10 and 15: "))
        game(score, guess)
    else:
        print("Thank you for playing")
        quit()
game(score, guess)