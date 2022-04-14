#Question 3b
entry = int(input("Enter a number between 0-20"))
count = 0
times_displayed = 0
while entry:
    if 1 > entry or entry > 20:
        count = count + 1
        entry = int(input("Enter a number between 0-20"))
    elif 1 < entry < 20:
        while count != -1:
            print(1+times_displayed)
            times_displayed = times_displayed + 1
            count = count - 1
        print("Goodjob")
        quit()
