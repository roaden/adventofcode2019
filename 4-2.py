#On the fourth day of advent...

min = 273025
max = 767253

criteria = 0

for i in range(min, max+1):
    work = str(i)
    lenwork = len(work)
    #check for doubles
    gotDubs = False
    gotDec = False
    for i in range(lenwork-1):
        if work[i] == work[i+1]:
            #check for neighbors
            gotNeighbors = False
            if i > 0:
                if work[i] == work[i-1]:
                    gotNeighbors = True
            if i < (lenwork - 2):
                if work[i+1] == work[i+2]:
                    gotNeighbors = True
            if gotNeighbors == False:
                gotDubs = True
                break
    if gotDubs:
        for i in range(lenwork-1):
            if int(work[i]) > int(work[i+1]):
                gotDec = True
                break
        if not gotDec:
            criteria += 1

print(criteria)
