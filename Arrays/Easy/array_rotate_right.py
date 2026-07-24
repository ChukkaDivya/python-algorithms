def right_rotate_one(nums):
    n = len(nums)
    if n <= 1:
        return nums
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp
    return nums
nums = [1,2,3,4,5]
print(right_rotate_one(nums))