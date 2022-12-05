textFile = open('2022/3-2022-text.txt', 'r')
textLines = textFile.readlines()
dupeLetter = list()
tripleLetter = list()
total = 0
P2total = 0

for line in textLines:
    length = int(len(line) / 2)
    part1 = line[0:length]
    part2 = line[length:len(line)]
    
    found = False
    for letter in part1:
        for secondLetter in part2:
            if letter == secondLetter and not found:
                dupeLetter.append(letter)
                found = True

for i in range(int(len(textLines) / 3)):
    foundP2 = False
    for letter in textLines[i * 3]:
        for secondLetter in textLines[(i * 3) + 1]:
            for thirdLetter in textLines[(i * 3) + 2]:
                if not foundP2 and letter == secondLetter and letter == thirdLetter:
                    tripleLetter.append(letter)
                    foundP2 = True
                        
for i in dupeLetter:
    temp = ord(i) - 96
    if temp < 0:
        temp += 58
    total += temp
    print(i)
    print(temp)
print(total)

for i in tripleLetter:
    temp = ord(i) - 96
    if temp < 0:
        temp += 58
    P2total += temp
print(P2total)