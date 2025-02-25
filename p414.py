class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)  # Remove duplicates
        if len(nums) < 3:
            return max(nums)  # Return max if there aren't three distinct numbers
        return sorted(nums, reverse=True)[2]