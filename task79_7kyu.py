# Task
# Given an array/list [] of n integers , Arrange them in a way similar
# to the to-and-fro movement of a Pendulum
# The Smallest element of the list of integers , must come in center position of array/list.
# The Higher than smallest , goes to the right .
# The Next higher number goes to the left of minimum
# number and So on , in a to-and-fro manner similar to that of a Pendulum.
# !alt
# Notes
# Array/list size is at least 3 .
# In Even array size , The minimum element should be moved
# to (n-1)/2 index (considering that indexes start from 0)
# Repetition of numbers in the array/list could occur ,
# So (duplications are included when Arranging).

def pendulum(values):
    sorted_values = sorted(values)
    middle = [sorted_values[0]]
    right_side = sorted_values[1::2]
    left_side = sorted_values[2::2]
    return left_side[::-1] + middle + right_side



