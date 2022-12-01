textFile = open('2022/1-2022-text.txt', 'r')
textLines = textFile.readlines()

totalCals = list()
elfCals = 0
largestElfCals = 0
largestElfIndex = 0
grandTotalCals = 0

for line in textLines:
    if len(line) > 2:
        elfCals += int(line.strip())
    else:
        totalCals.append(elfCals)
        elfCals = 0

for i in range(len(totalCals)):
    if totalCals[i] > largestElfCals:
        largestElfCals = totalCals[i]
        largestElfIndex = i
        
totalCals.sort(reverse=True)
grandTotalCals = totalCals[0] + totalCals[1] + totalCals[2]
print(largestElfCals)
print(largestElfIndex)
print(grandTotalCals)