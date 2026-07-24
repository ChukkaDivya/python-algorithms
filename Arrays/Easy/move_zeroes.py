def move_zeroes(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j],nums[i]=nums[i],nums[j]
            j+=1
    return nums
nums1 = [0,1,0,3,12]
nums2 = [0]
nums3 = [1,2,3]
nums4 = [0,0,1]
nums5 = [4,0,5,0,0,3,0]
print(move_zeroes(nums1))
print(move_zeroes(nums2))
print(move_zeroes(nums3))
print(move_zeroes(nums4))
print(move_zeroes(nums5))