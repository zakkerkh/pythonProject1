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
