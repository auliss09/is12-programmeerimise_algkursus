# -*- coding: utf-8 -*-

# 1) paluda kasutajal tekst sisestada

tekst= raw_input("Palun sisesta siia oma tekst: ")
if any(a.isdigit() for a in tekst) and tekst.islower():
	print "Väiketähed ja numbrid"
elif any(a.isdigit() for a in tekst)==False and tekst.islower():
	print "Väiketähed ja numbriteta"
elif any(a.isdigit() for a in tekst) and tekst.isupper():
	print "Suured tähed ja numbrid"
elif any(a.isdigit() for a in tekst)==False and tekst.isupper():
	print "Suured tähed ja numbriteta"
else:
    if any(a.isdigit() for a in tekst) and any(a.isupper()for a in tekst) and any(a.islower()for a in tekst):
	   print "Suur- ja väiketähed ning numbrid"
    else:
	   print "Suur- ja väiketähed ning numbriteta"


# 2) kasutaja sisestab 2 arvu

arv1=int(raw_input('Sisesta siia I number: '))
arv2=int(raw_input('Sisesta siia II number: '))

i=0
absoluut=abs(arv1-arv2)
vastus=0
while i <= absoluut:
	i=i+1
	if i % 3 == 0:
		vastus=vastus+1
print 'Vahemikul ' + str(arv1) + ' kuni ' + str(arv2) + ' on ' + str(vastus) + ' kolmega jaguvat arvu'