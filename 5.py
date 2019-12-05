#read file
foo = open('input5.txt', 'r')

intStack = foo.readline().rstrip('\n').split(',')

for i in range(len(intStack)):
    intStack[i] = int(intStack[i])

#print(intStack)

opNum = 0

while opNum <= len(intStack):
    imm = [False, False, False]
    foo = str(intStack[opNum])
    #Okay, we gotta catch opcodes with immediate mode.
    if len(str(intStack[opNum])) > 2:
        print(foo)
        command = int(foo[-1])
        foo = foo[:-2]
        while len(foo) < 3: #pad them if no leading 0
            foo = '0' + foo
        for i in range(len(foo)):
            imm[i] = foo[i]
        print(imm, command)

    else:
        command = int(foo)
    if command == 99:
        break
    elif command == 1:
        foo = intStack[opNum + 1]
        bar = intStack[opNum + 2]
        baz = intStack[opNum + 3]
        if imm[2]:
            fooL = foo
        else:
            fooL = intStack[foo]
        if imm[1]:
            barL = bar
        else:
            barL = intStack[bar]
        intStack[baz] = fooL + barL
        forward = 4
    elif command == 2:
        foo = intStack[opNum + 1]
        bar = intStack[opNum + 2]
        baz = intStack[opNum + 3]
        if imm[2]:
            fooL = foo
        else:
            fooL = intStack[foo]
        if imm[1]:
            barL = bar
        else:
            barL = intStack[bar]
        intStack[baz] = fooL * barL
        forward = 4
    elif command == 3:
        foo = intStack[opNum+1]
        intStack[foo] = 1
        forward = 2
    elif command == 4:
        print(intStack[opNum+1])
        forward = 2
    else:
        print("Error, unexpected code encountered at " + str(opNum) + " with value " + str(intStack[opNum]))
        break
    opNum += forward

#print(intStack)
#print(intStack[0])
