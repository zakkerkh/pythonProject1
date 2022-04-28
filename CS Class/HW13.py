#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#28/04/2022
#Hello, how are you doing

#1
word1 = input("A Enter at least 2 characters: ")
while len(word1) < 2:
    word1 = input("B Enter at least 2 characters: ")
while word1 != "Exit":
    while len(word1) < 2:
        word1 = input("C Enter at least 2 characters: ")
    if word1 != "Exit":
        print((word1[-2] + word1[-1]) * 5)
        word1 = input("D Enter at least 2 characters: ")
    if word1 == "Exit":
        quit()

