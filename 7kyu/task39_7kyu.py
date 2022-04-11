# Introduction and Warm-up (Highly recommended)
# Playing With Lists/Arrays Series
# Task
# Given an array/list [] of integers , Find the product of the k maximal numbers.
# Notes
# Array/list size is at least 3 .
# Array/list's numbers Will be mixture of positives , negatives and zeros
# Repetition of numbers in the array/list could occur.

# [10,8,7,9], 3

def max_product(lst, n_largest_elements):
    count = 1
    for i in range(n_largest_elements):
        count *= max(lst)
        lst.remove(max(lst))
    return count

# print(max_product([10,8,7,9], 3))
