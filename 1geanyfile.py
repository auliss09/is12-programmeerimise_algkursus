#!/usr/bin/env python
# -*- coding: utf8 -*-
from random import randint

kuulid = ['s']*5 + ['m']*6 + ['v']*7
print kuulid
for i in xrange(100):
	min = 0
	max = len(kuulid)-1
	kuul = randint(min, max)
	kuul1 = kuulid[kuul]
	del kuulid[kuul]
	
	min = 0
	max = len(kuulid)-1
	kuul = randint(min, max)
	kuul2 = kuulid[kuul]
	del kuulid[kuul]
	
	kuulid = kuulid + [kuul1] + [kuul2]

print kuulid
