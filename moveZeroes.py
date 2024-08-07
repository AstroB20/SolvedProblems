def moveZeroes(nums:list):
    ct=len(nums)
    for i in range(ct):
        if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                print(nums)    
    print(nums)                
moveZeroes([0,1,0,12,0,22,3,4])
                  
                

        