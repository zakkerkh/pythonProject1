#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#13/04/2022
#Hello, how are you doing

#Question 1a
import random

age = int(input("What is your age?: "))

while age < 16:
    print("You are not old enough")
    age = int(input("What is your age?: "))
print("You are old enough to drive, goodbye!")

#Question 1b
age = int(input("What is your age:"))
while age:
    if age < 0 or age > 130:
        age = int(input("invalid entry, try again: "))
    elif age > 16:
        print("You are old enought to get a lisence")
        quit()
    else:
        age = int(input("You are too young"))

#Question 2a
rand = random.randint(1, 30)
print("the random number is", rand)
print("Enter a number larger than", rand)
entry = int(input())
while entry:
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        quit()

#Question 2b
rand = random.randint(1, 30)
print("the random number is", rand)
print("Enter a number larger than", rand)
entry = int(input())
while entry:
    if entry >= rand+50:
        entry = int(input("Invalid input, try again: "))
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        quit()

#Question 2c
rand = random.randint(1, 30)
print("the random number is", rand)
print("Enter a number larger than", rand)
entry = int(input())
while entry:
    if entry >= 50:
        entry = int(input("Invalid input, try again: "))
    if entry <= rand:
        entry = int(input("Sorry try again"))
    elif entry > rand:
        print("goodjob")
        max = entry
        print("Enter a number greater than", rand, "but less than", max)
        entry = int(input())
        while entry:
            if entry >= 50:
                entry = int(input("Invalid input, try again: "))
            if entry <= rand:
                entry = int(input("Sorry try again"))
            elif max > entry > rand:
                print("goodjob")

#Question 3a
entry = int(input("Enter a number between 0-20"))
while entry:
    if 1 > entry > 20:
        entry = int(input("Enter a number between 0-20"))
    elif 1 < entry < 20:
        print("goodjob")
        quit()

#Question 3b
entry = int(input("Enter a number between 0-20"))
count = 0
times_displayed = 0
while entry:
    if 1 > entry or entry > 20:
        count = count + 1
        entry = int(input("Enter a number between 0-20"))
    elif 1 < entry < 20:
        while count != -1:
            print(1+times_displayed)
            times_displayed = times_displayed + 1
            count = count - 1
        print("Goodjob")
        quit()

#Question 3c
entry = int(input("Enter a number between 0-20: "))
count = 0
times_displayed = 0
org_count = 0
while entry:
    if 1 > entry or entry > 20:
        count = count + 1
        entry = int(input("Enter a number between 0-20: "))
    elif 1 < entry < 20:
        while count != -1:
            print(1+times_displayed)
            org_count = org_count + 1 + times_displayed
            times_displayed = times_displayed + 1
            count = count - 1
        print(org_count)
        print("Goodjob")
        quit()

#Question 3d
entry = int(input("Enter 1st number between 1-20: "))
entry2 = int(input("Enter 2nd number between 1-20: "))
count = 0
store = 0
sum = 0
while 1 > entry or entry > 20:
    entry = int(input("Enter 1st number between 1-20: "))
while 1 > entry2 or entry2 > 20:
    entry2 = int(input("Enter 2nd number between 1-20: "))
    print("stuck")

if 1 < entry < 20 and 1 < entry2 < 20:
    if entry > entry2:
        store = entry
        entry = entry2
        entry2 = store
    num = entry2 - entry
    while count != num:
        print(entry + count)
        sum = sum + entry + count
        count = count + 1
    print(sum)

    print("Farewell")

#While II
#Question 1a
num = 10
while num != 0:
    print(num - 2)
    num = num - 2

#Question 1b
num = int(input("Enter a number greater than 1: "))
if num % 2 != 0:
    num = num + 1
while num != 2:
    print(num - 2)
    num = num - 2

#Question 1c
num = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2st number: "))
diff = 0

if num2 > num:
    num, num2 = num2, num
diff = num - num2

while diff < 3:
    print("The numbers are not 3 apart")
    num = int(input("Enter a 1st number: "))
    num2 = int(input("Enter a 2st number: "))
    if num2 > num:
        num, num2 = num2, num
    diff = num - num2

if num % 2 != 0:
    num = num + 1

while num != num2 + 2:
    print(num - 2)
    num = num - 2

#Question 2
mark = int(input("Enter a mark: "))
good_grades = 0
mark_count = 0
while mark != -1:
    mark = int(input("Enter a mark: "))
    mark_count = mark_count + 1

    if mark >= 70:
        good_grades += 1

if mark == -1:
    print(good_grades/mark_count*100, "% of the marks are above 70%")

#Question 3
num = int(input("Enter a number greater than 0:"))
count = 0
ans = "="

while num <= 0:
    num = int(input("Enter a number greater than 0: "))

num = str(num)
print(num + "!")

count = int(num)
while count != 0:
    if count == 1:
        temp_count = str(count)
        ans = ans + temp_count
        count = count - 1
        print(ans)
    else:
        temp_count = str(count)
        ans = ans + temp_count + "*"
        count = count - 1

num = int(num)
count1 = num
num_ans = num

while count1 != 1:
    num_ans = num_ans*(count1-1)
    count1 -= 1

print("=" + str(num_ans))

#Question 4
day = int(input("What day of the week is it? 1-Sun, 2-Mon, 3-Tues, 4-Wed, 5-Thur, 6-Fri, 7-Sat or 8-Vacation: "))

while day:
    if day == 1 or day == 7 or day == 8:
        print("You can sleep in")
        day = int(input("What day of the week is it? 1-Sun, 2-Mon, 3-Tues, 4-Wed, 5-Thur, 6-Fri, 7-Sat or 8-Vacation: "))
    if day == 2 or day == 3 or day == 4 or day == 5 or day == 6:
        print("You cannot sleep in")
        day = int(input("What day of the week is it? 1-Sun, 2-Mon, 3-Tues, 4-Wed, 5-Thur, 6-Fri, 7-Sat or 8-Vacation: "))
    if day == 0:
        quit()

#Question 5
num = int(input("First number: "))
num1 = int(input("Second number: "))

while num and num1:
    if num != num1:
        print(num+num1)
        num = int(input("First number: "))
        num1 = int(input("Second number: "))
    if num == num1:
        print(2*(num+num1))
        num = int(input("First number: "))
        num1 = int(input("Second number: "))
    if num and num1 == 0:
        quit()

#Question 6
num = random.randint(0, 30)
entry = int(input("Guess a number between 0 and 30: "))
score = 0
while entry and num:
    if entry >= num-2 and entry <= num+2:
        print("AMAZING")
        score += 6
        print(score)
        redo = input("Would you like to play again? y/n: ")
        if redo == "y":
            num = random.randint(0, 30)
            entry = int(input("Guess a number between 0 and 30: "))
        elif redo == "n":
            quit()
    if entry >= num-5 and entry <= num+5:
        print("Wow!")
        score += 4
        print(score)
        redo = input("Would you like to play again? y/n: ")
        if redo == "y":
            num = random.randint(0, 30)
            entry = int(input("Guess a number between 0 and 30: "))
        elif redo == "n":
            quit()

    if entry >= num-10 and entry <= num+10:
        print("Good Job")
        score += 2
        print(score)
        redo = input("Would you like to play again? y/n: ")
        if redo == "y":
            num = random.randint(0, 30)
            entry = int(input("Guess a number between 0 and 30: "))
        elif redo == "n":
            quit()
    else:
        print(score)
        redo = input("Would you like to play again? y/n: ")
        if redo == "y":
            num = random.randint(0, 30)
            entry = int(input("Guess a number between 0 and 30: "))
        elif redo == "n":
            quit()




