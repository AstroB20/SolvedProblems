class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = cur_min = result = nums[0]

        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)

            result = max(result, cur_max)

        return result
