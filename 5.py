#!/usr/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

max_dividers = [10, 20]


def is_evenly_divisible(num, up_to):
        for divider in range(1,up_to+1):
                if num % divider <> 0:
                        return False
        print '%d is evenly divisible to all nums from 1 to %d' % (num, up_to)
        return True


for max_divider in max_dividers:
        num = max_divider + 1
        while is_evenly_divisible(num, max_divider) == False:
                num += 1
                if num % 200000 == 0:
                        print 'Testing num %d' % num
        print '%d: from 1 to %d' % (num, max_divider)
