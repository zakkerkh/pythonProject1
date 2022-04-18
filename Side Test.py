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