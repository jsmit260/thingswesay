#!/usr/bin/python

import random


phrases=[]
with open('phrasefile.txt') as f:
    for line in f:
        phrases.append(line)



print(random.choice(phrases))
