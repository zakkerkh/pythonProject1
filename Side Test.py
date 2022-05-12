work = "shfdhfkdshfjkd"
entry = "kfgjkdshf"
del_count = 0

if len(entry) >= 5:
    if (work[0] and work[1] and work[2] and work[3]) == work[4]:
        entry = entry[del_count+5:]
elif len(entry) >= 4:
    elif (work[0] and work[1] and work[2]) == work[3]:
        entry = entry[del_count+4: ]
elif len(entry) >= 3:
    elif (work[0] and work[1]) == work[2]:
        entry = entry[del_count+4:]
elif len(entry) >= 2:
    else:
        work = work[1:]
        del_count += 1
elif len(entry) >= 1:
    else:
        work = work[1:]
        del_count += 1