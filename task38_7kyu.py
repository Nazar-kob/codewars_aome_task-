# Task
# Given an array of integers ,
# Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
# Notes
# Array/list size is at least 2.
# Array/list numbers could be a mixture of positives, negatives also zeroes .


def adjacent_element_product(array):
    return max([array[i] * array[i + 1] for i in range(len(array) - 1)])


ls = [3, 6, -2, -5, 7, 3]

adjacent_element_product(ls)
