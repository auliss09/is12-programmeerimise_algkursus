#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

def kursor(x,y,tekst):
	sys.stdout.write("\033["+str(y)+";"+str(x)+"H" + tekst)

def box(x,y,h,w):
	i=1
	j=1
	while j <= h:
		kursor(x+j,y, "#")
		kursor(x+h,y+j, "#")
		while i <= w:
			kursor(y+i,x+h, "#")
			kursor(y+x,y+w, "#")
			i=i+1
		j=j+1
box(10,10,10,10)

sys.stdout.flush()
time.sleep(3)




"""
	kursor(x,y,"#")
	kursor(x+w,y, "#")
	kursor(y+w,x+h, "#")
	kursor(y,y+w, "#")
"""
