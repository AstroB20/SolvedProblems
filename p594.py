class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        max_length = 0
        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])
        return max_length
    
