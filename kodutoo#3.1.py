print "Kas {0} saad aru v6i ei {1}?".format("Sa", "saa")

a = "I am a {0}".format("python string")
print a

print "{:.2f}".format(3.1414926)
print "{:+.2f}".format(3.1415926) 
print "{:+.2f}".format(-1) 
print "{:.0f}".format(2.71828)
print "{:0>2d}".format(5) 
print "{:x<4d}".format(5) 
print "{:x<4d}".format(10) 
print "{:,}".format(1000000) 
print "{:.2%}".format(0.25) 
print "{:.2e}".format(1000000000) 
print "{:10d}".format(13) 
print "{:<10d}".format(13) 
print "{:^10d}".format(13) 


print "{0:d} - {0:x} - {0:o} - {0:b} ".format(51)

meil = "Sinu meiliaadress on {email}".format
print meil(email="sinunimi@midaiganes.com")

lause = "Ma {verb} oma {object} {place} peale.".format(verb="panin", object="arvuti", place="laua")
print lause

print "{} koht lauses on m2rgitud enamasti {{0}}-ga".format("Tyhi")

loom1 = "Kassid"
loom2 = "koerad"
print "%s ja %s elavad koos" % (loom1,loom2)

print "Oh {0}, {0}! wherefore art thou {0}?".format("Romeo")
 
