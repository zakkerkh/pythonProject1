#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#28/03/2022
#Hello, how are you doing

var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))

if var1 > 15 or var2 >15:
    print(var1+var2)
if var1+var2>15:
    print(var1*var2)
else:
    print(var1-var2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if 1<num1<10 and 1<num2<10 and num2<=0:
    print("True")
elif num2<=0 and 1>num1>10:
    print("True")
elif num2==0:
    print("Maybe")
