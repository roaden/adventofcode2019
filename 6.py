#get orbits

fin = open('input6.txt', 'r')

orbits = []
for line in fin:
    orbits.append(line.strip('\n').split(')'))

objects = []
for orbit in orbits:
    objects.append(orbit[0])
    objects.append(orbit[1])

objects = list(set(objects))

planets = []
moons = []

for n in range(len(orbits)):
    planets.append(orbits[n][0])
    moons.append(orbits[n][1])

def orbitsWhat(moon):
#Need to write function
#return False if orbits nothing
#return what it orbits
       try:
           num = moons.index(moon)
           return planets[num]
       except ValueError:
           return False


numOrbits = 0

for moon in objects:
    stillOrbiting = True
    while(stillOrbiting):
        foo = orbitsWhat(moon)
        if foo != False:
            numOrbits += 1
            moon = foo
        else:
            stillOrbiting = False

print(numOrbits)
