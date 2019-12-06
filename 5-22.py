#get the stack

fin = open('input5.txt', 'r')

stack = []

for line in fin:
    stack.append(int(line.strip('\n')))

def immTest( num ):
    imm = [False, False, False]
    newNum = num
    if len(str(num)) > 2:
        work = str(num)
        newNum = int(work[-2:])
        immMap = work[:-2]
        while len(immMap) < 3:
            immMap = '0' + immMap
        imm[0] = (immMap[2] == '1')
        imm[1] = (immMap[1] == '1')
        imm[2] = (immMap[0] == '1')
    immMap.append(newNum)
    return immMap

