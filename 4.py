#!/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(product):
        product_as_list = list(str(product))
        reverted_list = list(product_as_list)
        reverted_list.reverse()
#        print 'Product : %s' % ''.join(product_as_list)
#        print 'Reverse : %s' % ''.join(reverted_list)
        return product_as_list == reverted_list


max_i = 0
max_j = 0
max_product = 0

for i in xrange(100, 1000):
        for j in xrange(100, 1000):
                ixj = i*j
                print 'i: %d, j: %d, ixj: %d' % (i, j, ixj)
                if is_palindrome(ixj) == True:
                        if ixj > max_product:
                                max_product = ixj
                                max_i = i
                                max_j = j

print 'i: %d j: %d' % (max_i, max_j)

