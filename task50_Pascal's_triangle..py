# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number
# is the sum of the two numbers directly above it as shown:
from math import factorial


def generate(numRows):
    result = []
    for i in range(numRows):
        position = []
        for j in range(i + 1):
            position.append(factorial(i) // (factorial(j) * factorial(i - j)))
        result.append(position)
    return result
