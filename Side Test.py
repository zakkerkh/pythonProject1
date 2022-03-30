import math

challenge = input("Would you like a challenge question y/n: ")

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
num3 = random.randint(-6, 8)

operator1 = random.randint(1, 7)
operator2 = random.randint(1, 7)

#1:+   2:-  3:*  4:**  5:/  6:// 7:%

if challenge == "n":
    quit()
elif challenge == "y":
    if operator1 == 1:
        num4 = num1+num2
        if operator2 == 1:
            ans=(num4+num3)
        elif operator2 == 2:
            ans=(num4-num3)
        elif operator2 == 3:
            ans=(num4 * num3)
        elif operator2 == 4:
            ans=(num4 ** num3)
        elif operator2 == 5:
            ans=(num4 / num3)
        elif operator2 == 6:
            ans=(num4 // num3)
        elif operator2 == 7:
            ans=(num4 % num3)
    if operator1 == 2:
        num4 = num1-num2
        if operator2 == 1:
            ans=(num4+num3)
        elif operator2 == 2:
            ans=(num4-num3)
        elif operator2 == 3:
            ans=(num4 * num3)
        elif operator2 == 4:
            ans=(num4 ** num3)
        elif operator2 == 5:
            ans=(num4 / num3)
        elif operator2 == 6:
            ans=(num4 // num3)
        elif operator2 == 7:
            ans=(num4 % num3)
    if operator1 == 3:
        num4 = num1*num2
        if operator2 == 1:
            ans=(num4+num3)
        elif operator2 == 2:
            ans=(num4-num3)
        elif operator2 == 3:
            ans=(num4 * num3)
        elif operator2 == 4:
            ans=(num4 ** num3)
        elif operator2 == 5:
            ans=(num4 / num3)
        elif operator2 == 6:
            ans=(num4 // num3)
        elif operator2 == 7:
            ans=(num4 % num3)
    if operator1 == 4:
        num4 = num1**num2
        if operator2 == 1:
            ans=(num4+num3)
        elif operator2 == 2:
            ans=(num4-num3)
        elif operator2 == 3:
            ans=(num4 * num3)
        elif operator2 == 4:
            ans=(num4 ** num3)
        elif operator2 == 5:
            ans=(num4 / num3)
        elif operator2 == 6:
            ans=(num4 // num3)
        elif operator2 == 7:
            ans=(num4 % num3)
    if operator1 == 5:
        num4 = num1/num2
        if operator2 == 1:
            ans=(num4+num3)
        elif operator2 == 2:
            ans=(num4-num3)
        elif operator2 == 3:
            ans=(num4 * num3)
        elif operator2 == 4:
            ans=(num4 ** num3)
        elif operator2 == 5:
            ans=(num4 / num3)
        elif operator2 == 6:
            ans=(num4 // num3)
        elif operator2 == 7:
            ans=(num4 % num3)
    if operator1 == 6:
        num4 = num1//num2
        if operator2 == 1:
            ans=(num4+num3)
        elif operator2 == 2:
            ans=(num4-num3)
        elif operator2 == 3:
            ans=(num4 * num3)
        elif operator2 == 4:
            ans=(num4 ** num3)
        elif operator2 == 5:
            ans=(num4 / num3)
        elif operator2 == 6:
            ans=(num4 // num3)
        elif operator2 == 7:
            ans=(num4 % num3)
    if operator1 == 7:
        num4 = num1%num2
        if operator2 == 1:
            ans=(num4+num3)
        elif operator2 == 2:
            ans=(num4-num3)
        elif operator2 == 3:
            ans=(num4 * num3)
        elif operator2 == 4:
            ans=(num4 ** num3)
        elif operator2 == 5:
            ans=(num4 / num3)
        elif operator2 == 6:
            ans=(num4 // num3)
        elif operator2 == 7:
            ans=(num4 % num3)
