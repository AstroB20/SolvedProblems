class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  #Expected output: 4
print(sol.search([1, 2, 3, 4, 5], 6))  