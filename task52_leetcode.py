# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must be unique
# and you may return the result in any order.

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(i for i in nums1 if i in nums2))