#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import time
import sys

def tarnid(x,y, txt):
	a=0
	while a<100:
		x=randint(0,70)
		y=randint(0,20)
		sys.stdout.write("\033["+str(y)+";"+str(x)+"H" + txt)
		a=a+1
tarnid(70,20, "*")

sys.stdout.flush()
time.sleep(6)
