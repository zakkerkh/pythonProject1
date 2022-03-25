#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#25/03/2022
#Hello, how are you doing

mark = int(input("What is your grade?: "))

if mark > 100 or mark < 0:
    print("Invalid entry")
elif mark > 90:
    print("You are doing an excellent job!")
elif mark > 80:
    print("Work harder and you can do better")
elif mark > 50:
    print("You are passing")
elif mark > 0:
    print("You are failing")