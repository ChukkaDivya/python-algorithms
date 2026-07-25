def rearrange_array(nums):
    n=len(nums)
    ans=[0]*n
    positive_index=0
    negative_index=1
    for num in nums:
        if num>0:
            ans[positive_index]=num
            positive_index+=2
        else:
            ans[negative_index]=num
            negative_index+=2
    return ans
print(rearrange_array([3,1,-2,-5,2,-4]))
print(rearrange_array([-1,1]))
print(rearrange_array([1,-1]))
print(rearrange_array([5,-2,4,-7]))