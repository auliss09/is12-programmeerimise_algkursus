#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

def kursor(x,y,tekst):
	sys.stdout.write("\033["+str(y)+";"+str(x)+"H" + "#")

def box(x,y,h,w):
	kursor(x,y,"#")
	kursor(x+w,y, "#")
	kursor(y+w,x+h, "#")
	kursor(y,y+w, "#")
		
box(10,10,12,12)

sys.stdout.flush()
time.sleep(6)
