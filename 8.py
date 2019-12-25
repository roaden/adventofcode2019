#Lookin at pitchurs

pixelWidth = 25
pixelHeight = 6

fin = open('input8.txt', 'r')

pict = fin.readline().strip('\n')

picSize = pixelWidth * pixelHeight

numPics = len(pict) // picSize

pics = []

for i in range(numPics):
    start = i*picSize
    end = start+picSize
    pics.append(pict[start:end])

leastZeroes = picSize+1

numLeast = 0

for i in range(len(pics)):
    zeroes = 0
    for char in pics[i]:
        if char == '0':
            zeroes += 1
    if zeroes < leastZeroes:
        numLeast = i
        leastZeroes = zeroes

num1 = 0
num2 = 0

for c in pics[numLeast]:
    if c == '1':
        num1 += 1
    elif c == '2':
        num2 += 1

print(num1 * num2)
