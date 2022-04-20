#g

entry = int(input("Enter a 3 digit number: "))
while entry != -1:
    while not(-1 and entry >= 100 and entry <= 999):
        entry = int(input("Enter a 3 digit number: "))

    num3 = entry%10
    num2 = entry%100//10
    num1 = entry//100

    print(num3)
    print(num2)
    print(num1)

    sum1 = num1+num2+num3

    print("The sum is:", sum1)

    count = 900
    starter = 99
    count1 = 0
    while count != 0:
        starter += 1

        var3 = starter % 10
        var2 = starter % 100 // 10
        var1 = starter // 100

        sum2 = var1+var2+var3
        if sum2 == sum1:
            count1 += 1

        count -= 1
    print("Count:", count1)
    entry = int(input("Enter a 3 digit number: "))
    print("Goodbye")
