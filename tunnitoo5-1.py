#!/usr/bin/python

from random import randint

kuulid = ['s']*5 + ['m']*6 + ['v']*7
min = 0
max = len(kuulid)-1
kuul = randint(min, max)
kuul1 = kuulid[kuul]
del kuulid[kuul]
print kuul1

min = 0
max = len(kuulid)-1
kuul = randint(min, max)
kuul2 = kuulid[kuul]
del kuulid[kuul]
print kuul2
