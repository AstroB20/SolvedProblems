def firstMissingPositive(nums:list):
#     least=1
#     while least in nums:
#         least+=1
#     return least
# print(firstMissingPositive([0,2,3,4,5]))
    nums.sort()
    index=0
    least=1
    if len(nums)==1:
        if nums[0]==1:
            return 2
        else:
            return 1
    while nums[index]<1:
        if index<len(nums):
            index+=1
        else: 
            return 1
    if nums[index]!=1:
        return 1
    for i in range(index,len(nums)-1):
        if nums[i+1]-nums[i]!=1:
            return nums[i]+1
    return nums[-1]+1
        
print(firstMissingPositive([-1,-2,-3]))