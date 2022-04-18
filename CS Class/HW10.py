#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#13/04/2022
#Hello, how are you doing

num1 = int(input("First starting number: "))
num2 = int(input("Second starting number: "))

print("The necklace is: ")

var1 = (num1 + num2) % 10
var2 = (var1 + num2) % 10

ans = str(num1) + str(num2) + str(var1) + str(var2)

while var1 and var2:
    if var1 != num1 or var2 != num2:
        var1 = (var1 + var2) % 10
        var2 = (var1 + var2) % 10
        ans += str(var1) + str(var2)

    elif var1 == num1 and var2 == num2:
        print(ans)
        quit()
