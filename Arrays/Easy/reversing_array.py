def reverse_array(nums):
    left=0
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums
print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array([1, 2, 3, 4]))
print(reverse_array([7]))
print(reverse_array([]))
print(reverse_array([10, -5, 0, 8, -2]))