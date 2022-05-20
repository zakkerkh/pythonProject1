#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#20/05/2022
#Hello, how are you doing

myList = [3, 4, 8, 11, 15]
count = 0

while count != len(myList):
    count += 1
    print("Item", count, "is:", myList[count-1])

myList = [3, 4, 8, 11, 15]
count = 0
num = 0

while count != len(myList):
    num += myList[count]
    count += 1

print(num)