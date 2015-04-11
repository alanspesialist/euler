#!/usr/bin/python

sum = 2
first = 1
second = 2
next = 0

while next < 4000000:
        next = first + second
        print 'Next: %d' % next
        if next % 2 == 0 and next < 4000000:
                sum += next
        first = second
        second = next
        

print 'sum = %d' % sum
