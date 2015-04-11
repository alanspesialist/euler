#!/usr/bin/python

# What is the largest prime factor of the number 600851475143

nums = [13195, 600851475143]


def is_prime(num):
        if num == 1:
                return False
        if num % 2 == 0:
                return False
        for jakaja in range(3,int(num**0.5)+1, 2):
                if num % jakaja == 0:
                        return False
        return True

for num in nums:
        largest_factor = 0
        for factor in range(3,int(num**0.5)+1, 2):
                if num % factor == 0:
                        if is_prime(factor) == True:
                                largest_factor = factor

        print 'Largest factor for num %d is %d' % (num, largest_factor)
