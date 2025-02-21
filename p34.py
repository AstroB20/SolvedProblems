def searchRange(nums, target):
    def findBound(isFirst):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    first = findBound(True)
    if first == -1:
        return [-1, -1]
    last = findBound(False)
    return [first, last]

print(searchRange([1,3,3,4,5,6,7,7,7,7,8,9],7))