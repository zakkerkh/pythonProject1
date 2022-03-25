age = int(input("What is your age?: "))

if age <= 0:
    print("Invalid entry")
elif age < 3:
    print("Toddler")
elif age < 10:
    print("Child")
elif age < 12:
    print("Preteen")
elif age < 18:
    print("Teen")
else:
    print("Adult")