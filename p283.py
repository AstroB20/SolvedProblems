def moveZeroes(nums):
    for n in nums:
        if n == 0:
            nums.remove(n)
            nums.append(0)
    return nums 
print(moveZeroes([0,1,0,3,12]))