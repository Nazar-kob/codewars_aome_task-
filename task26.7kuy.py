# Task
# You are given a sequence of positive ints where every
# element appears three times, except one that appears
# only once (let's call it x) and one that appears only twice (let's call it y).
# Your task is to find x * x * y.
# Example
# For arr=[1, 1, 1, 2, 2, 3], the result should be 18
# 3 x 3 x 2 = 18
# For arr=[6, 5, 4, 100, 6, 5, 4, 100, 6, 5, 4, 200], the result should be 4000000
# 200 x 200 x 100 = 4000000

def missing_values(seq):
    x = [i for i in seq if seq.count(i) == 1][0]
    y = [i for i in seq if seq.count(i) == 2][0]
    return x * x * y
