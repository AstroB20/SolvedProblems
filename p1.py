class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h_map={}
        for index , val in enumerate(nums):
            diff = target - val
            if diff in h_map:
                return [index,h_map[diff]]
            h_map[val] = index
        