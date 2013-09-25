#!/usr/bin/python

from random import randint

kuulid = ['s']*5 + ['m']*6 + ['v']*7

n = len(kuulid)-1
kuul = randint(0,n)
kuul1 = kuulid[kuul]
del kuulid[kuul]
print kuul1

n = len(kuulid)-1
kuul = randint(0,n)
kuul2 = kuulid[kuul]
del kuulid[kuul]
print kuul2
