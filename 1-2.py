#import the file
foo = open("1-1.txt", 'r')
def fuelNeeded(num):
    return max(num//3-2,0)

totalFuel = 0

for line in foo:
    weight = int(line)
    while(weight > 0):
        weight = fuelNeeded(weight)
        totalFuel += weight

print(totalFuel)
