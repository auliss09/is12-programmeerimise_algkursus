#!/usr/bin/python

from random import randint

klass = ['kairo', 'aigar', 'timo', 'mario', 'ardo', 'mariin', 'egert', 'jasper']
#print klass

#length = len(klass)
#x=length-1
#print klass [randint(0,x)]

#min=0
#max=len(klass)-1
#n=randint(min,max)
#print klass [n]

#v6i print klass[randint(0,len(klass)-1)]

print klass
del klass [3]
print klass

karp = ['a', 'b', 'c', 'd']
print karp
n=1
element=karp[n]
del karp[n]
karp = karp + [element]
print karp
