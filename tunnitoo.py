#!/usr/bin/python

from random import randint

kuulid = ['s']*5 + ['m']*10 + ['v']*15

print randint(1,3)

print kuulid [randint(0,29)]

i=randint(0,29)
print kuulid [i]

for n in xrange (10):
	print n

for n in kuulid:
	print n


