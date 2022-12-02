# Had to do a decent amount of research and stack overflow to find the solution to this
# Clueless to how hexadecimal works, but hashlib knows

import hashlib

n = 1
zeroes = 5 # part 1
zeroes = 6 # part 2
prefix = zeroes * '0'

while True:
    s = "yzbqklnj" + str(n)
    h = hashlib.md5(s.encode()).hexdigest()[:zeroes]
    if h == prefix:
        print(n)
        exit()
    n += 1
    