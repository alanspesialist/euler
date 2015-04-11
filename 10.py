#!/usr/bin/python

def is_prime(num):
        if num == 1:
                return False
        if num % 2 == 0:
                return False
        for jakaja in range(3,int(num**0.5)+1, 2):
                if num % jakaja == 0:
                        return False
        return True

sum = 0
#for number in range (1,11):
for number in range (1,2000001):
        if number % 10000 == 0:
                print number
        if is_prime(number) == True:
                sum += number
#                print "%d is a prime" % number

print sum + 2
