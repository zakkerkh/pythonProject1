#Question 3
num = int(input("Enter a number greater than 0:"))
count = 0
ans = ""
while num <= 0:
    num = int(input("Enter a number greater than 0: "))

print(num + "!")

count = num
while count != 0:
    ans = num + "*"
print("=", num, "")
