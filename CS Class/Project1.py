#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#12/05/2022
#Hello, how are you doing

entry = input("What are you letters?")
work = entry
del_count = 0

if (work[0] and work[1] and work[2] and work[3]) == work[4]:
    entry = entry[del_count+5:]
elif (work[0] and work[1] and work[2]) == work[3]:
    entry = entry[del_count+4:]
elif (work[0] and work[1]) == work[2]:
    entry = entry[del_count+4:]
else:
    work = work[1:]
    del_count += 1

if (work[0] and work[1] and work[2] and work[3]) == work[4]:
    entry = entry[del_count+5:]
elif (work[0] and work[1] and work[2]) == work[3]:
    entry = entry[del_count+4:]
elif (work[0] and work[1]) == work[2]:
    entry = entry[del_count+4:]
else:
    work = work[1:]

print(work)
