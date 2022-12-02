textFile = open('2022/2-2022-text.txt', 'r')
textLines = textFile.readlines()

score = 0
part2Score = 0

for line in textLines:
    opponent = line[0]
    you = line[2]
    
    if you == 'X':
        score += 1
        if opponent == 'A':
            score += 3
            part2Score += 3
        elif opponent == 'C':
            score += 6
            part2Score += 2
        else:
            part2Score += 1
    elif you == 'Y':
        score += 2
        part2Score += 3
        if opponent == 'A':
            score += 6
            part2Score += 1
        elif opponent == 'B':
            score += 3
            part2Score += 2
        else:
            part2Score += 3
    else:
        score += 3
        part2Score += 6
        if opponent == 'B':
            score += 6
            part2Score += 3
        elif opponent == 'C':
            score += 3
            part2Score += 1
        else:
            part2Score += 2

print(score)
print(part2Score)