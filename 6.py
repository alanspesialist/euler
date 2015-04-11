#!/usr/bin/python

def sum_of_squares(count):
        sum = 0
        for num in range(1,count):
                sum += num ** 2
        return sum

def square_of_sum(count):
        sum = 0
        for num in range(1,count):
                sum += num
        return sum ** 2

print square_of_sum(101) - sum_of_squares(101)
