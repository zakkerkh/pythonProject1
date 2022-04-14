entry = int(input("Enter a number between 0-20"))
while entry:
    if entry > 20 or entry < 0:
        entry = int(input("Enter a number between 0-20"))
    elif 1 < entry < 20:
        print("goodjob")
        quit()
