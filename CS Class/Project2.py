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
         "the clue is at your desk", "the clue is in the washroom", "the clue is in the lobby",
         "the clue is in the security desk", "the clue is in the conference room", "the clue is in the parking lot"
]
clue_hint = ["michael", "annex", "reception",
             "desk", "washroom", "lobby",
             "security desk", "conference", "parking lot"
]

success = False
while not success:
    clue_choice = random.randint(0, len(clues)-1)
    clue_hint_choice = clue_choice
    text1 = clues[clue_choice]
    new_text = ""
    count1 = 0

    while count1 != len(text1):
        if text1[count1] != " ":
            new_text += alphabet[new_alphabet[alphabet.index(text1[count1])]]

        if text1[count1] == " ":
            new_text += " "

        count1 += 1

    print(new_text.capitalize())
    print("Your hint is", clue_hint[clue_hint_choice])

    print("Enter the location you would like to go\n")
    print("Michael's Office-1      Your Desk-4       Security Desk-7")
    print("Annex-2                 Washroom-5        Conference Room-8")
    print("Reception-3             Lobby-6           Parking Lot-9")

    location = input("Input: ")

    if location == clue_choice

    success = True
