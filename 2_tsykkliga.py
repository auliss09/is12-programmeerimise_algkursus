x=0
while x<100:
	print "{0:02d}".format(x),
	x=x+1
	while x%10==9:
		print "{0:02}".format(x)+ "\n"
		x=x+1
print ""
