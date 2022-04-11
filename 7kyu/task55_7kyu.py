# You are given an odd-length array of integers,
# in which all of them are the same, except for one single number.
# Complete the method which accepts such an array,
# and returns that single different number.
# The input array will always be valid! (odd-length >= 3)


def stray(arr):
    result_list = list(set(arr))
    return result_list[0] if arr.count(result_list[0]) > 1 else result_list[1]
