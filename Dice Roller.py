import random
rolli = input("Would you like to roll the dice? Yes/No")


rlist = ["Yes", "yes", "y"]
nrlist = ["No", "no", "n"]
alist = nrlist + rlist

if rolli in nrlist:
    print("Very well, I have no idea why you ran this program...")
    quit()

elif rolli not in alist:
    print("Invalid Entry")
    quit()

def dice():
    rollt = int(input("How many rolls would you like? "))
    roll = "rolin" + rollt * "g"
    if rolli in rlist:
        print(roll)
        while rollt != 0:
            rollt = rollt - 1
            print(random.randint(1, 6))

print(dice())

def redo(rolla):
    if rolla in nrlist:
        print("Thank you for playing, have a good day!")
        quit()
    elif rolla not in alist:
        print("Invalid Entry")
        quit()
    elif rolla in rlist:
        print(dice())
        rolla = input("Would you desire to roll again?")
        print(redo(rolla))

print(redo(rolla = input("Would you desire to roll again?")))
