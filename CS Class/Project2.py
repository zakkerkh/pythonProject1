#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#31/05/2022
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

clues = ["the clue is in michaels office", "the clue is in the annex", "the clue is at reception",
         "the clue is at your desk", "the clue is in the conference room"
]

clue_choice = random.randint(0, len(clues)-1)
text1 = clues[clue_choice]
new_text = ""
count1 = 0
while count1 != len(text1):
    if text1[count1] != " ":
        new_text += alphabet[new_alphabet[alphabet.index(text1[count1])]]

    if text1[count1] == " ":
        new_text += " "

    count1 += 1

print(new_text)

print("Your hint is")

