def max_subarray(nums):
    max_sum=nums[0]
    current_sum=nums[0]
    for i in range(1,len(nums)):
        current_sum=max(nums[i],current_sum+nums[i])
        max_sum=max(current_sum,max_sum)
    return max_sum
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))   # 6
print(max_subarray([1]))                        # 1
print(max_subarray([5,4,-1,7,8]))              # 23
print(max_subarray([-5,-2,-8]))                # -2
print(max_subarray([2,-1,2,3,-9,4]))           # 6