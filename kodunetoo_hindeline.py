#!/usr/bin/env python
# -*- coding: utf8 -*-

# arvude keskmine

arvud = (41,24)  
keskmine = sum(arvud)/float(len(arvud)) 
print "Arvude 41 ja 24 keskmine on: " + str(keskmine) 

print""
print "----------------------------------------"
print""

# fibonacci

def fibonacci(n):
	fib = [0, 1]
	for i in range(2, n+1):
		fib.append(fib[-1] + fib[-2])
	return fib

print fibonacci(20)

print""
print "----------------------------------------"
print""

# ruutvõrrand

def ruutfunktsioon():
	a=1
	b=-3
	c=-4
	print "Ruutvõrrandiks on: x^2-3x-4=0"
	print ""
	juur = (b*b)-4*(a*c)
	ac = 4*(a*c)
	bb = b*b
	a2 = a*2
	if juur < ac:
		print "Lahendid puuduvad!"
	else:
		ruutjuur = juur**.5
		x1=-(float(b))+ruutjuur
		x2=-(float(b))-ruutjuur
		x1=float(x1)/float(a2)
		x2=float(x2)/float(a2)
		print "Selle ruutvõrrandi lahendid on:" 
		print [x1,x2]
ruutfunktsioon()
