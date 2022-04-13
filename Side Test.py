import random
#Question 2a
rand = random.randint(1, 30)
print("the random number is", rand)
print("Enter a number larger than", rand)
entry = int(input())
while entry:
    if entry >= rand+50:
        entry = int(input("Invalid input, try again: "))
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        quit()