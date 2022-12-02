textFile = open('2015/3-2015-text.txt', 'r')
textLines = textFile.readlines()

directions = textLines[0]

xPos = 0
yPos = 0
roboXPos = 0
roboYPos = 0

visitedX = list()
visitedY = list()

visitedX.append(0)
visitedY.append(0)

for i in range(len(directions)):
    alreadyVisited = False
    if directions[i] == '^':
        if i % 2 == 0:
            yPos += 1
        else:
            roboYPos += 1
    elif directions[i] == 'v':
        if i % 2 == 0:
            yPos -= 1
        else:
            roboYPos -= 1
    elif directions[i] == '>':
        if i % 2 == 0:
            xPos += 1
        else:
            roboXPos += 1
    else:
        if i % 2 == 0:
            xPos -= 1
        else:
            roboXPos -= 1
        
    for j in range(len(visitedX)):
        if i % 2 == 0:
            if xPos == visitedX[j] and yPos == visitedY[j]:
                alreadyVisited = True
        else:
            if roboXPos == visitedX[j] and roboYPos == visitedY[j]:
                alreadyVisited = True
    
    if not alreadyVisited:
        if i % 2 == 0:
            visitedX.append(xPos)
            visitedY.append(yPos)
        else:
            visitedX.append(roboXPos)
            visitedY.append(roboYPos)

print(len(visitedX))