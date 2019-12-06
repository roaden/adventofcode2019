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

foo = True

def orbitPath(moon):
    path = []
    foo = orbitsWhat(moon)
    while True:
        if foo == False:
            break
        else:
            path.append(foo)
            foo = orbitsWhat(foo)
    return path

santaPath = orbitPath('SAN')
youPath = orbitPath('YOU')


while True:
    if santaPath[-1] == youPath[-1]:
        del santaPath[-1]
        del youPath[-1]
    else:
        break

print(len(santaPath) + len(youPath))
