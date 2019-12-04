#read file
foo = open('2-1.txt', 'r')

intStack = foo.readline().rstrip('\n').split(',')

for i in range(len(intStack)):
    intStack[i] = int(intStack[i])

intStack[1] = 12
intStack[2] = 2

print(intStack)

opNum = 0

while opNum <= len(intStack):
    if intStack[opNum] == 99:
        break
    elif intStack[opNum] == 1:
        foo = intStack[opNum + 1]
        bar = intStack[opNum + 2]
        baz = intStack[opNum + 3]
        intStack[baz] = intStack[foo] + intStack[bar]
    elif intStack[opNum] == 2:
        foo = intStack[opNum + 1]
        bar = intStack[opNum + 2]
        baz = intStack[opNum + 3]
        intStack[baz] = intStack[foo] * intStack[bar]
    else:
        print("Error, unexpected code encountered at " + str(opNum) + " with value " + str(intStack[opNum]))
        break
    opNum += 4

print(intStack)
print(intStack[0])
