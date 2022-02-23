


color = input("what is you favorite color:")
person = input("think of a random person:")
random = input("random object")

print("zokorila's favorite color is "+ color)
print(person + " is the first thing that comes to your mind")
print("you favorite material thing is " + random)







import random
Lowest = int(input("What is the lowest number "))
Highest = int(input("What is your highest number "))

number = random.randint(Lowest, Highest)

print("The random number is", number)



from math import *

numb = -9
print(pow(numb, 8))
print(min(numb, 219043824, 9))
print(round(84793.89734568))
print(sqrt(2))


def say_hi():
    print("Hello", input("What is your name: "))
say_hi()


def cube(numb):
    return numb*numb*numb
result =  cube(int(input("What number do you want to cube: ")))
print(result)

is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are only male")
elif not(is_male) and is_tall:
    print("You are only tall")
else:
    print("you are not male and tall")



def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

val1 = int(input("What is Your First Number:"))
val2 = int(input("What is Your Second Number:"))
val3 = int(input("What is Your Third Number:"))
print(max_num(val1, val2, val3))

var1 = float(input("First Number: "))
op = input("Enter Operator: ")
var2 = float(input("Third Number: "))

if op == "+":
    print(var1 + var2)
elif op == "-":
    print(var1 - var2)
elif op == "/":
    print(var1 / var2)
elif op == "*":
    print(var1 * var2)
else:
    print("Invalid Operator")


monthconv = {
    "Jan": "January",
    "Feb": "Febraury",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
}

var1 = input("What Month:")
print(monthconv[var1])
print(monthconv.get("jing", "Not sehr gut entry"))

i = int(input("Choose a Number:"))
while i< 10:
    print("Thats kinda small", i)
    i += 1

while i == 10:
    print("Thats the one", i)
    i += 1

print("Thats it")


secword = "cow"
guess = ""
gcount = 0
guessl = 5
oofgs = False
while guess != secword and not(oofgs):
   if gcount < guessl:
    guess = input("Enter Guess: ")
    gcount += 1
   else:
       oofgs = True


if oofgs:
    print("You are und loser")
else:
    print("you guessed the secret word")


fries = ["jim", "karen", "kevin"]
len(fries)
for index in range(9):
    print(index)
b_numb =float(input("Base Number:"))
p_numb =float(input("Power Number:"))

def exp(b_numb, p_numb):
    return b_numb**p_numb

print(exp(b_numb,p_numb))

def exp(b_numb, p_numb):
    result = 1
    for index in range(p_numb):
        result = result * b_numb
    return result

print(exp(3, 7))


numb_g = [
    [1, 2 , 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(numb_g[0][1])
for row in numb_g:
    for dol in row:
        print(dol)


def trans(phr):
    translation = ""
    for letter in phr:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(trans("dingery"))

import random

suff = ["stein", "burg", "schlag"]
wor = random.choice(suff)

entr = input("What is the word you want to translate?")


def magdeutch(phra):
    translation = ""
    if entr[-1] == "g":
        translation = entr + "ery"
    else:
        translation = phra + wor
    return translation

print(magdeutch(entr))

import random
rolli = input("Would you like to roll the dice? Yes/No? ")


rlist = ["Yes", "yes", "y"]
nrlist = ["No", "no", "n"]

if rolli in nrlist:
    print("Very well, I have no idea why you ran this program...")
    quit()

elif rolli not in rlist or nrlist:
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

    elif rolli not in rlist or nrlist:
        print("Invalid Entry")
        quit()

    elif rolla in rlist:
        print(dice())
        rolla = input("Would you desire to roll again?")
        print(redo(rolla))

print(redo(rolla = input("Would you desire to roll again?")))



import random
import string

print("Welcome to your glorious homemade password generator!")

len = int(input("How long do you want the password to be?: "))

rlist = ["Yes", "yes", "y"]
nrlist = ["No", "no", "n"]

l = input("Do you want lowercase letters?: ")
u = input("Do you want uppercase letters?: ")
n = input("Do you want numbers?: ")
s = input("Do you want symbols?: ")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

if l in nrlist:
    lower = None
elif l in rlist:
    lower = string.ascii_lowercase

if u in nrlist:
    upper = None
elif u in rlist:
    upper = string.ascii_uppercase

if n in nrlist:
    num = None
elif n in rlist:
    num = string.digits

if s in nrlist:
    symbols = None
elif s in rlist:
    symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, len)
password = "".join(temp)
print(password)



