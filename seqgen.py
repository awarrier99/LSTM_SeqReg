import string
from random import *

alpha = string.ascii_lowercase

pats = ["ABC", "ABB", "CAB", "BAC", "CBB", "ACB"]
rules = {0:3, 2:5, 3:2, 1:4, 5:1, 4:0}


def createRand(x):
    for i in range(0, 100):
        x += alpha[randint(0, 25)]
    return x

def seqGen(x, pats, start = 0):
    done = False
    pos = randint(0, 8)
    ind = start
    pat = pats[start]
    while (not done):
        if pos > len(x) - 3:
            break
        x = x[:pos] + pat + x[pos + 3:]
        off = randint(8, 18)
        pos += off
        ind = rules[ind]
        pat = pats[ind]
    return x

with open("data.txt", 'a') as op:
    op.seek(0)
    op.truncate()
    for j in range(0, 20):
        op.write(seqGen(createRand(""), pats) + '\n')
