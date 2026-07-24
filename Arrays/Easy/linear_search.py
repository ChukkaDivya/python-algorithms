def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
print(linear_search([5, 8, 2, 9, 1],9))