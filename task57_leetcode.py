# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

from task50_Pascal_s_triangle import generate


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return generate(rowIndex + 1)[-1]


if __name__ == '__main__':
    one = Solution()
    print(one.getRow(3))
