#!/usr/bin/python

from random import randint

klass = ['Aigar', 'Aleks', 'Ardo', 'Art', 'Arti', 'Aulis', 'Egert', 'Eveli', 'Janar', 'Janis', 'Jasper', 'Kairo', 'Katerin', 'Kerto', 'Mariin', 'Mario', 'Rait', 'Timo']

min = 0
max = len(klass)-1
opilane = randint(min, max)
element = klass[opilane]
del klass[opilane]
klass = klass + [element]
print klass




#klassi nimekirja ylesanne:
#* massiiv klassi nimekirjaga, t2hestikuline
#* v6tta massiivist v2lja suvaline element
#* lisada massiivi l6ppu
#teha seda kokku 100x.
#trykkida v2lja massiiv

