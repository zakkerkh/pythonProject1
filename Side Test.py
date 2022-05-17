entry = input("Enter a 7 character number string:")
guess = input("Guess what the output will be all consecutive triplets are removed")
count = 0
count1 = 0
points = 0
redo = "y"
list = "You entered: " + entry

right = "You got it right! "
wrong = "You got it wrong... "
while redo == "y":
    while count < 10:
        if len(entry) >= 3 and entry[0] == entry[1] == entry[2]:
            entry = entry[3:]
            count1 += 1
        elif len(entry) >= 4 and entry[1] == entry[2] == entry[3]:
            entry = entry[0:1] + entry[4:]
            count1 += 1
        elif len(entry) >= 5 and entry[2] == entry[3] == entry[4]:
            entry = entry[0:2] + entry[5:]
            count1 += 1
        elif len(entry) >= 6 and entry[3] == entry[4] == entry[5]:
            entry = entry[0:3] + entry[6:]
            count1 += 1
        elif len(entry) >= 7 and entry[4] == entry[5] == entry[6]:
            entry = entry[0:4] + entry[7:]
            count1 += 1

        count += 1

    print(entry)
    list = list + " the answer is " + entry

    if guess == entry:
        print(right)
        list += " " + right + ","
        points += 1
    else:
        print(wrong)
        list += wrong + ","

    redo = input("Would you like to play again? y/n: ")
    if redo == "y":
        entry = input("Enter a 7 character number string:")
        guess = input("Guess what the output will be all consecutive triplets are removed")
        count = 0
        count1 = 0
        list += "You entered: " + entry + ":"

print("Final results: " + list)