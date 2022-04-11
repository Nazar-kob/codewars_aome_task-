# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than
# ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement( nums):
    result = {nums.count(i): i for i in set(nums)}
    return result[max(result)]
