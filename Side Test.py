#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#20/05/2022
#Hello, how are you doing
import random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
new_alphabet = []

count = 0
while count != 26:
    num = random.randint(0, 25)

    while num in new_alphabet:
        num = random.randint(0, 25)
    new_alphabet.append(num)

    count += 1

new_text = ""
text1 = input("jdhgksdhg")
count1 = 0

while count1 != len(text1):
    if text1[count1] != " ":
        new_text += alphabet[new_alphabet[alphabet.index(text1[count1])]]

    if text1[count1] == " ":
        new_text += " "
    count1 += 1
count1 = 0

print(new_text)