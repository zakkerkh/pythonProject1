entry = int(input("Enter 1st number between 0-20: "))
entry2 = int(input("Enter 1st number between 0-20: "))
count = 0
times_displayed = 0
org_count = 0
while entry:
    if 1 > entry or entry > 20:
        count = count + 1
        entry = int(input("Enter a number between 0-20: "))
    elif 1 < entry < 20:
        while count != -1:
            print(1+times_displayed)
            org_count = org_count + 1 + times_displayed
            times_displayed = times_displayed + 1
            count = count - 1
        print(org_count)
        print("Goodjob")
        quit()

