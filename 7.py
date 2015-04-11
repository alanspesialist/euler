#!/usr/bin/python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

nums = [6, 10001]


def is_prime(num):
        if num == 1:
                return False
        if num == 2:
                return True
        if num % 2 == 0:
                return False
        for jakaja in range(3,int(num**0.5)+1, 2):
                if num % jakaja == 0:
                        return False
        return True

for n in nums:
        counter = 0
        num_to_be_tested = 1
        while True:
                if is_prime(num_to_be_tested) == True:
                        print '%d is prime' % num_to_be_tested
                        counter += 1
                if counter == n:
                        break
                num_to_be_tested += 1

        print '%dth prime number is %d' % (n, num_to_be_tested)
