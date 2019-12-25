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

masterImage='2' * picSize

masterImage = list(masterImage)

for i in range(len(masterImage)):
    layer = 0
    while masterImage[i] == '2':
        masterImage[i] = pics[layer][i]
        layer += 1

for i in range(pixelHeight):
    for j in range(pixelWidth):
        print(masterImage[i*pixelWidth + j], end='')
    print()

for i in range(len(masterImage)):
    if masterImage[i] == '0':
        print(' ', end='')
    elif masterImage[i] == '1':
        print('0', end='')
    if i%pixelWidth == pixelWidth-1:
        print()

print()
