def removeElement(nums:list, val):
    ctVal=nums.count(val)
    new=[]
    for i in nums:
        if i!=val:
            new.append(i)
    for i in range(ctVal):
        new.append(0)
        print(new)
    return new

removeElement([3,2,2,3],3)
        