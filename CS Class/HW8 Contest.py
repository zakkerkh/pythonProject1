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

print("What is", num1, "/", num2)
question5 = int(input())
if question5 == num1/num2:
    print("You got the right answer")
    score = score+1
elif question5==num1/num2+1 or question5==num1/num2-1:
    print("You are close")
    print("the correct answer was", num1 / num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 / num2)

print("What is", num1, "//", num2)
question6 = int(input())
if question6 == num1//num2:
    print("You got the right answer")
    score = score+1
elif question6==num1//num2+1 or question6==num1//num2-1:
    print("You are close")
    print("the correct answer was", num1 // num2)
else:
    print("Sorry that was wrong")
    print("the correct answer was", num1 // num2)

print("What is", num1, "%", num2)
question7 = int(input())
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


