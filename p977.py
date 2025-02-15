class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sqList = [nums ** 2 for nums in nums]
        sqList.sort()
        return sqList
        