textFile = open('2022/4-2022-text.txt', 'r')
textLines = textFile.readlines()

total = 0
secondTotal = 0

for line in textLines:
    count = 0
    firstElf1 = ""
    firstElf2 = ""
    secondElf1 = ""
    secondElf2 = ""
    for letter in range(len(line.strip())):
        if line[letter] == "-" or line[letter] == ",":
            count += 1
        elif count == 0:
            firstElf1 += line[letter]
        elif count == 1:
            firstElf2 += line[letter]
        elif count == 2:
            secondElf1 +=line[letter]
        elif count == 3:
            secondElf2 += line[letter]

    if (int(firstElf1) <= int(secondElf1) and int(firstElf2) >= int(secondElf2)) or (int(firstElf1) >= int(secondElf1) and int(firstElf2) <= int(secondElf2)):
        total += 1
        print(f"{firstElf1},{firstElf2}-{secondElf1},{secondElf2}")
    if (int(firstElf1) <= int(secondElf1) and int(firstElf2) >= int(secondElf1)) or (int(secondElf1) <= int(firstElf1) and int(secondElf2) >= int(firstElf1)):
        secondTotal += 1
    elif (int(firstElf1) <= int(secondElf2) and int(firstElf2) >= int(secondElf2)) or (int(secondElf1) <= int(firstElf2) and int(secondElf2) >= int(firstElf2)):
        secondTotal += 1
print(total)
print(secondTotal)
            