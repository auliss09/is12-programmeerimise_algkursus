#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

def kursor(x,y,tekst):
	sys.stdout.write("\033["+str(y)+";"+str(x)+"H" + "#")

def box(x,y,h,w):
	i=1
	j=1
	while j <= h:
		kursor(x+j,y, "#")   		# ylemine
		kursor(x+h,y+j, "#") 		# parem kylg
		while i <= w:
			kursor(y+i,x+h, "#")	# alumine
			kursor(y+x,y, "#")		# vasak kylg ?
			i=i+1
		j=j+1
box(10,10,10,10)

sys.stdout.flush()
time.sleep(3)
