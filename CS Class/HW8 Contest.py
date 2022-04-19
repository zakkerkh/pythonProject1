#Zakariyah. M. J. Khan & Amir S
#ICS2O_2122_S2
#28/03/2022
#Hello, how are you doing
import random

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
score = 0

print("What is", num1, "+", num2)
question1 = float(input())
if question1 == num1+num2:
    print("You got the right answer")
    score = score+1
elif question1==num1+num2+1 or question1==num1+num2-1:
    print("You are close")
    print("the correct answer was", num1 + num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 + num2)

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
print("What is", num1, "-", num2)
question2 = float(input())
if question2 == num1-num2:
    print("You got the right answer")
    score = score+1
elif question2==num1-num2+1 or question2==num1-num2-1:
    print("You are close")
    print("the correct answer was", num1 - num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1-num2)

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
print("What is", num1, "*", num2)
question3 = float(input())
if question3 == num1*num2:
    print("You got the right answer")
    score = score+1
elif question3==num1*num2-1 or question3==num1*num2-1:
    print("You are close")
    print("the correct answer was", num1 * num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 * num2)

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
print("What is", num1, "**", num2)
question4 = float(input())
if question4 == num1**num2:
    print("You got the right answer")
    score = score+1
elif question4==num1**num2+1 or question4==num1**num2-1:
    print("You are close")
    print("the correct answer was", num1 ** num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 ** num2)

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
while num2 == 0:
    num2 = random.randint(-6, 8)
print("What is", num1, "/", num2)
question5 = float(input())
if question5 == num1/num2:
    print("You got the right answer")
    score = score+1
elif question5==num1/num2+1 or question5==num1/num2-1:
    print("You are close")
    print("the correct answer was", num1 / num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 / num2)

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
while num2 == 0:
    num2 = random.randint(-6, 8)
print("What is", num1, "//", num2)
question6 = float(input())
if question6 == num1//num2:
    print("You got the right answer")
    score = score+1
elif question6==num1//num2+1 or question6==num1//num2-1:
    print("You are close")
    print("the correct answer was", num1 // num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 // num2)

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
print("What is", num1, "%", num2)
question7 = float(input())
if question7 == num1%num2:
    print("You got the right answer")
    score = score+1
elif question7==num1%num2+1 or question7==num1%num2-1:
    print("You are close")
    print("the correct answer was", num1 % num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 % num2)

print(score, "/ 7")

challenge = input("Would you like a challenge question y/n: ")

num1 = random.randint(-6, 8)
num2 = random.randint(-6, 8)
num3 = random.randint(-6, 8)

operator1 = random.randint(1, 7)
operator2 = random.randint(1, 7)

#1:+   2:-  3:*  4:**  5:/  6:// 7:%

if challenge == "n":
    quit()

elif not("y" or "n"):
    print("invalid Entry")

while challenge == "y" or redo == 1:
    challenge = "blah"
    if operator1 == 1:
        num4 = num1+num2
        if operator2 == 1:
            ans=(num4+num3)
            print(str(num1) + "+" + str(num2) + "+" + str(num3))
        elif operator2 == 2:
            ans=(num4-num3)
            print(str(num1) + "+" + str(num2) + "-" + str(num3))
        elif operator2 == 3:
            ans=(num4 * num3)
            print(str(num1) + "+" + str(num2) + "*" + str(num3))
        elif operator2 == 4:
            ans=(num4 ** num3)
            print(str(num1) + "+" + str(num2) + "^" + str(num3))
        elif operator2 == 5:
            ans=(num4 / num3)
            print(str(num1) + "+" + str(num2) + "/" + str(num3))
        elif operator2 == 6:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 // num3)
            print(str(num1) + "+" + str(num2) + "//" + str(num3))
        elif operator2 == 7:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 % num3)
            print(str(num1) + "+" + str(num2) + "%" + str(num3))
    if operator1 == 2:
        num4 = num1-num2
        if operator2 == 1:
            ans=(num4+num3)
            print(str(num1) + "-" + str(num2) + "+" + str(num3))
        elif operator2 == 2:
            ans=(num4-num3)
            print(str(num1) + "-" + str(num2) + "-" + str(num3))
        elif operator2 == 3:
            ans=(num4 * num3)
            print(str(num1) + "-" + str(num2) + "*" + str(num3))
        elif operator2 == 4:
            ans=(num4 ** num3)
            print(str(num1) + "-" + str(num2) + "^" + str(num3))
        elif operator2 == 5:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 / num3)
            print(str(num1) + "-" + str(num2) + "/" + str(num3))
        elif operator2 == 6:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 // num3)
            print(str(num1) + "-" + str(num2) + "//" + str(num3))
        elif operator2 == 7:
            ans=(num4 % num3)
            print(str(num1) + "-" + str(num2) + "%" + str(num3))
    if operator1 == 3:
        num4 = num1*num2
        if operator2 == 1:
            ans=(num4+num3)
            print(str(num1) + "*" + str(num2) + "+" + str(num3))
        elif operator2 == 2:
            ans=(num4-num3)
            print(str(num1) + "*" + str(num2) + "-" + str(num3))
        elif operator2 == 3:
            ans=(num4 * num3)
            print(str(num1) + "*" + str(num2) + "*" + str(num3))
        elif operator2 == 4:
            ans=(num4 ** num3)
            print(str(num1) + "*" + str(num2) + "^" + str(num3))
        elif operator2 == 5:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 / num3)
            print(str(num1) + "*" + str(num2) + "/" + str(num3))
        elif operator2 == 6:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 // num3)
            print(str(num1) + "*" + str(num2) + "//" + str(num3))
        elif operator2 == 7:
            ans=(num4 % num3)
            print(str(num1) + "*" + str(num2) + "%" + str(num3))
    if operator1 == 4:
        num4 = num1**num2
        if operator2 == 1:
            ans=(num4+num3)
            print(str(num1) + "^" + str(num2) + "+" + str(num3))
        elif operator2 == 2:
            ans=(num4-num3)
            print(str(num1) + "^" + str(num2) + "-" + str(num3))
        elif operator2 == 3:
            ans=(num4 * num3)
            print(str(num1) + "^" + str(num2) + "*" + str(num3))
        elif operator2 == 4:
            ans=(num4 ** num3)
            print(str(num1) + "^" + str(num2) + "^" + str(num3))
        elif operator2 == 5:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 / num3)
            print(str(num1) + "^" + str(num2) + "/" + str(num3))
        elif operator2 == 6:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 // num3)
            print(str(num1) + "^" + str(num2) + "//" + str(num3))
        elif operator2 == 7:
            ans=(num4 % num3)
            print(str(num1) + "^" + str(num2) + "%" + str(num3))
    if operator1 == 5:
        num4 = num1/num2
        if operator2 == 1:
            ans=(num4+num3)
            print(str(num1) + "/" + str(num2) + "+" + str(num3))
        elif operator2 == 2:
            ans=(num4-num3)
            print(str(num1) + "/" + str(num2) + "-" + str(num3))
        elif operator2 == 3:
            ans=(num4 * num3)
            print(str(num1) + "/" + str(num2) + "*" + str(num3))
        elif operator2 == 4:
            ans=(num4 ** num3)
            print(str(num1) + "/" + str(num2) + "^" + str(num3))
        elif operator2 == 5:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 / num3)
            print(str(num1) + "/" + str(num2) + "/" + str(num3))
        elif operator2 == 6:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 // num3)
            print(str(num1) + "/" + str(num2) + "//" + str(num3))
        elif operator2 == 7:
            ans=(num4 % num3)
            print(str(num1) + "/" + str(num2) + "%" + str(num3))
    if operator1 == 6:
        while num2 == 0:
            num2 = random.randint(-6, 8)
        num4 = num1//num2
        if operator2 == 1:
            ans=(num4+num3)
            print(str(num1) + "//" + str(num2) + "+" + str(num3))
        elif operator2 == 2:
            ans=(num4-num3)
            print(str(num1) + "//" + str(num2) + "-" + str(num3))
        elif operator2 == 3:
            ans=(num4 * num3)
            print(str(num1) + "//" + str(num2) + "*" + str(num3))
        elif operator2 == 4:
            ans=(num4 ** num3)
            print(str(num1) + "//" + str(num2) + "^" + str(num3))
        elif operator2 == 5:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 / num3)
            print(str(num1) + "//" + str(num2) + "/" + str(num3))
        elif operator2 == 6:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 // num3)
            print(str(num1) + "//" + str(num2) + "//" + str(num3))
        elif operator2 == 7:
            ans=(num4 % num3)
            print(str(num1) + "//" + str(num2) + "%" + str(num3))
    if operator1 == 7:
        num4 = num1%num2
        if operator2 == 1:
            ans=(num4+num3)
            print(str(num1) + "%" + str(num2) + "+" + str(num3))
        elif operator2 == 2:
            ans=(num4-num3)
            print(str(num1) + "%" + str(num2) + "-" + str(num3))
        elif operator2 == 3:
            ans=(num4 * num3)
            print(str(num1) + "%" + str(num2) + "*" + str(num3))
        elif operator2 == 4:
            ans=(num4 ** num3)
            print(str(num1) + "%" + str(num2) + "^" + str(num3))
        elif operator2 == 5:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 / num3)
            print(str(num1) + "%" + str(num2) + "/" + str(num3))
        elif operator2 == 6:
            while num3 == 0:
                num3 = random.randint(-6, 8)
            ans=(num4 // num3)
            print(str(num1) + "%" + str(num2) + "//" + str(num3))
        elif operator2 == 7:
            ans=(num4 % num3)
            print(str(num1) + "%" + str(num2) + "%" + str(num3))

        user_ans = int(input("What is the answer?: "))
        if user_ans==ans:
            print("You got it right!")
            redo = int(input("Would you like to play again? 1- Yes 2 -No: "))
        else:
            print(ans)
            print("That was wrong")
            redo = int(input("Would you like to play again? 1- Yes 2 -No: "))


