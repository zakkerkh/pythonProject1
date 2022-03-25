import random
#Question 3


score = 0

def game(score):
    number = random.randint(10, 15)
    print(number)
    guess = int(input("Guess a number between 10 and 15: "))

    if guess==number:
        score = score+3
        print("You got it")
        print(score)
    else:
        score = score-1
        print(score)
        print("Try again")
    play = input("Would you like to play again y/n?: ")
    if play == "y":
        game(score)
    else:
        print("Thank you for playing")
        quit()
game(score)