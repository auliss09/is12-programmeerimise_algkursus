print '{0}, {1}, {2}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format(*'abc')
print '{0}{1}{0}'.format('abra', 'cad')

print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print 'Coordinates: {latitude}, {longitude}'.format(**coord)

c = 3-5j
('The complex number {0} is formed from the real part {0.real} '
'and the imaginary part {0.imag}.').format(c)
class Point(object):
		def __init__(self, x, y):
			self.x, self.y = x, y
		def __str__(self):
			return 'Point({self.x}, {self.y})'.format(self=self)
print str(Point(4, 2))

coord = (3, 5)
print 'X: {0[0]};  Y: {0[1]}'.format(coord)

print  "repr() shows quotes: {0!r}; str() doesn't: {1!s}".format('test1', 'test2')

print '{0:<30}'.format('left aligned')
print '{0:>30}'.format('right aligned')
print '{0:^30}'.format('centered')
print '{0:*^30}'.format('centered') #koos t2rnidega

print '{0:+f}; {0:+f}'.format(3.14, -3.14)
print '{0: f}; {0: f}'.format(3.14, -3.14)
print '{0:-f}; {0:-f}'.format(3.14, -3.14)

print "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(32)
print "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(32)

points = 19.5
total = 22
print 'Correct answers: {0:.2%}.'.format(points/total)

import datetime
d = datetime.datetime(2013, 9, 15, 18, 19, 36)
print '{0:%Y-%m-%d %H:%M:%S}'.format(d)

octets = [192, 168, 0, 1]
print '{0:02X}{1:02X}{2:02X}{3:02X}'.format(*octets)

width = 5
for num in range(5,12):
 for base in 'dXob':
	 print '{0:{width}{base}}'.format(num, base=base, width=width)
 print
