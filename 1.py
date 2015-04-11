#!/usr/bin/python

sum = 0
for num in range(1,1000):
	print 'num: %d' % num
	if num % 3 == 0 or num % 5 == 0:
		sum += num

print 'sum = %d' % sum
