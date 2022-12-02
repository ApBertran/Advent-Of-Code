textFile = open('2015/5-2015-text.txt', 'r')
textLines = textFile.readlines()

part1GoodStrings = 0
part2GoodStrings = 0

# Parameters:
vowels = ('a', 'e', 'i', 'o', 'u')
forbidden = ('ab', 'cd', 'pq', 'xy')

for line in textLines:
    test1 = False # 3 vowels
    test2 = False # double letter
    test3 = True # no forbidden combinations
    test4 = False # repeat two letters
    test5 = False # repeat with letter in between
    previousLetter = ''
    twoLettersAgo = ''
    numVowels = 0
    
    for letterCount in range(len(line)):
        # test 1
        for vowel in vowels:
            if line[letterCount] == vowel:
                numVowels += 1
            if numVowels >= 3:
                test1 = True

        if letterCount > 0:
            # test 2
            if line[letterCount] == previousLetter:
                test2 = True
            # test 3
            for badCombo in forbidden:
                if previousLetter + line[letterCount] == badCombo:
                    test3 = False
                    
    # Part 2
        if letterCount > 1:
            # test 4
            for prevLetters in range(letterCount - 1):
                if prevLetters > 0:
                    if previousLetter + line[letterCount] == line[prevLetters - 1] + line[prevLetters]:
                        test4 = True
                        print(f"First: {previousLetter + line[letterCount]}")
                        print(f"Match: {line[prevLetters - 1] + line[prevLetters]}")
                        print(line)
            # test 5
            if line[letterCount] == twoLettersAgo:
                test5 = True
                    
        previousLetter = line[letterCount]
        twoLettersAgo = line[letterCount - 1]
    
    if test1 and test2 and test3:
        part1GoodStrings += 1
    if test4 and test5:
        part2GoodStrings += 1

print(f"Part 1: {part1GoodStrings}")
print(f"Part 2: {part2GoodStrings}")