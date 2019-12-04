fin = open('3-1.txt', 'r')

first = fin.readline().strip('\n')
second = fin.readline().strip('\n')

first = first.split(',')
second = second.split(',')

dir1 = []
dist1 = []
dir2 = []
dist2 = []

for i in first:
    dir1.append(i[0])
    dist1.append(int(i[1:]))

for i in second:
    dir2.append(i[0])
    dist2.append(int(i[1:]))


def makeCoords(dirs, dists):
    x = [0]
    y = [0]
    for i in range(len(dirs)):
        if dirs[i] == 'R':
            x.append(x[i] + dists[i])
            y.append(y[i])
        elif dirs[i] == 'L':
            x.append(x[i] - dists[i])
            y.append(y[i])
        elif dirs[i] == 'U':
            x.append(x[i])
            y.append(y[i] + dists[i])
        elif dirs[i] == 'D':
            x.append(x[i])
            y.append(y[i] - dists[i])
        else:
            print("Unexpected value at ", i, " of ", dirs[i])
            break
    coords = [x, y]
    return coords

def checkIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x2 and x3 == x4:
        if x1 != x3:
            return False
        else:
            print("Write the horizontal code.")
            return False
    elif y1 == y2 and y3 == y4:
        if y1 != y3:
            return False
        else:
            print("Write the vertical code.")
            return False
    elif x1 == x2:
        xint = x1
        yint = y3
        if min(x3,x4) <= xint <= max(x3,x4) and min(y1,y2) <= yint <= max(y1,y2):
            print("Found intersect at ", xint, " , ", yint)
            return abs(xint) + abs(yint)
        else:
            return False
    elif y1 == y2:
        xint = x3
        yint = y1
        if min(x1,x2) <= xint <= max(x1,x2) and min(y3,y4) <= yint <= max(y3,y4):
            print("Found intersect at ", xint, " , ", yint)
            return abs(xint) + abs(yint)
        else:
            return False

coords1 = makeCoords(dir1,dist1)
coords2 = makeCoords(dir2, dist2)

lengths = []
for i in range(0,len(dir1)):
    for j in range(0,len(dir2)):
        x1 = coords1[0][i]
        x2 = coords1[0][i+1]
        x3 = coords2[0][j]
        x4 = coords2[0][j+1]
        y1 = coords1[1][i]
        y2 = coords1[1][i+1]
        y3 = coords2[1][j]
        y4 = coords2[1][j+1]
        foo = checkIntersect(x1, y1, x2, y2, x3, y3, x4, y4)
        if foo != False:
            lengths.append(foo)

print(lengths)
print(min(lengths))
