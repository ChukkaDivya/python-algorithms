def max_subarray(nums):
    max_sum=float('-inf')
    current_sum=0
    for num in nums:
        current_sum+=num
        max_sum=max(max_sum,current_sum)
        if current_sum<0:
            current_sum=0
    return max_sum
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))   # 6
print(max_subarray([1]))                        # 1
print(max_subarray([5,4,-1,7,8]))              # 23
print(max_subarray([-5,-2,-8]))                # -2
print(max_subarray([2,-1,2,3,-9,4]))           # 6