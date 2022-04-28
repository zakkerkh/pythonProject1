#2
word1 = input("A Enter at least 2 characters: ")
while word1:
    while len(word1) < 2:
        word1 = input("A Enter at least 2 characters: ")
    if word1 != "Exit":
        print((word1[-2] + word1[-1]) * 5)
        word2 = input("A Enter at least 4 characters: ")
        while word2:
            while len(word2) < 2:
                word1 = input("A Enter at least 2 characters: ")
            if word1 != "Exit":
                print((word2[-2] + word2[-1]) * 5)


