#!/usr/bin/python

# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?



def calculate_chain(num):
        length = 1
        while num != 1:
                if num % 2 == 0:
                        # even
                        num = num / 2
                else:
                        # odd
                        num = 3 * num + 1
                length += 1
        return length


longest_chain = 0
starting_number = 1
the_number = 1

while starting_number < 1000000:
        chain_len = calculate_chain(starting_number)
        if chain_len > longest_chain:
                longest_chain = chain_len
                the_number = starting_number
                print 'Found longer chain: %d with starting number %d' % (chain_len, starting_number)
        starting_number += 1

print 'Longest chain: %d with starting number %d' % (longest_chain, the_number)
