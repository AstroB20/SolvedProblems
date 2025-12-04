class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = max_sum = nums[0]
        for n in nums[1:]:
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)
        return max_sum