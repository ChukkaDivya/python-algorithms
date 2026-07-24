def remove_duplicates(nums):
    if len(nums)==0:
        return 0
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
        
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [1]
nums4 = [1,1,1,1]
for i in [nums1,nums2,nums3,nums4]:
    terms=remove_duplicates(i)
    print(i[:terms])