def threeSumClosest(nums, target):
    n=len(nums)
    res=[0,0,0]
    minDiff=float('inf')
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                currSum = nums[i] + nums[j] + nums[k]
                currDiff = abs(currSum - target)
                if currDiff < minDiff:
                    minDiff = currDiff
                    res = [nums[i], nums[j], nums[k]]
    return sum(res)
print(threeSumClosest([-1,2,1,-4],1))
