word1 = input("Enter a words 4 at least 4 characters long: ")

while word1 != "end":
    print(str.capitalize(word1[2: 5] + word1[0:2] + word1[5: ]))
    word1 = input("Enter a words 4 at least 4 characters long: ")

print("Goodbye")