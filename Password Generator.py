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