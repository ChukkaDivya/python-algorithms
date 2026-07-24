def left_rotate_one(nums):
    n = len(nums)
    if n <= 1:
        return nums
    temp = nums[0]
    for i in range(n-1):
        nums[i] = nums[i+1]
    nums[n - 1] = temp
    return nums
nums = [1,2,3,4,5]
print(left_rotate_one(nums))