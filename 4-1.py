#On the fourth day of advent...

min = 273025
max = 767253

criteria = 0

for i in range(min, max+1):
    work = str(i)
    #check for doubles
    gotDubs = False
    gotDec = False
    for i in range(len(work)-1):
        if work[i] == work[i+1]:
            gotDubs = True
            break
    if gotDubs:
        for i in range(len(work)-1):
            if int(work[i]) > int(work[i+1]):
                gotDec = True
                break
        if not gotDec:
            criteria += 1

print(criteria)
