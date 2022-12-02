textFile = open('2015/2-2015-text.txt', 'r')
textLines = textFile.readlines()

count = 0
totalSurfaceArea = 0
totalRibbon = 0

for line in textLines:
    chrctrCount = 0
    lastKnown = 0
    xCount = 0
    l = 0
    w = 0
    for chrctr in line:
        chrctrCount += 1
        if chrctr == 'x':
            if xCount == 0:
                l = int(line[0:chrctrCount - 1])
                lastKnown = chrctrCount
            elif xCount == 1:
                w = int(line[lastKnown:chrctrCount - 1])
                lastKnown = chrctrCount
            xCount += 1
    h = int(line[lastKnown:chrctrCount - 1])
    
    sides = list()
    sides.append(int(2 * l * w))
    sides.append(int(2 * w * h))
    sides.append(int(2 * l * h))
    smallestSide = int(min(sides) / 2)
    surfaceArea = sides[0] + sides[1] + sides[2] + smallestSide
    totalSurfaceArea += surfaceArea
    dimensions = list()
    dimensions.append(l)
    dimensions.append(w)
    dimensions.append(h)
    dimensions.sort()
    ribbon = int((dimensions[0] * 2) + (dimensions[1] * 2) + (l * w * h))
    totalRibbon += ribbon

print(totalSurfaceArea)
print(totalRibbon)
