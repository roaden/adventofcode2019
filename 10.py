#Gonna need trig, woo.
import math

#open the file with the map.

fin = open('input10.txt', 'r')

starMap = []

for line in fin:
    starMap.append(list(line.strip('\n')))


maxSight = 0
maxX = -1
maxY = -1

#Check each spot for asteroids
roids = []

for i in range(len(starMap)):
    for j in range(len(starMap)):
        if starMap[i][j] == '#':
            roids.append([i,j])

for a in roids:
    angles = []
    for b in roids:
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        angles.append(math.atan2(dy,dx))
    #Now get rid of extra angles.
    angles = list(set(angles))
    if len(angles) > maxSight:
        maxSight = len(angles)
        maxX = a[0]
        maxY = a[1]

print('Your best spot is at ' + str(maxX) + ' , ' + str(maxY) 
        + " with " + str(maxSight) + ' lines of sight.')
