#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

tekst=raw_input("Sisesta tekst: ")

def kursor(x,y,tekst):
	sys.stdout.write("\033["+str(y)+";"+str(x)+"H" + tekst)
kursor(34,12,tekst)
