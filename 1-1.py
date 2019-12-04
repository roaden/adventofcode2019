#import the file
foo = open("1-1.txt", 'r')
def fuelNeeded(num):
    return num//3-2

totalFuel = 0

for line in foo:
    totalFuel += fuelNeeded(int(line))

print(totalFuel)
