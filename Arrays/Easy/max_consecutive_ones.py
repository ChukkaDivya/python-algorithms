def max_consecutive_ones(nums):
    count=0
    max_count=0
    for num in nums:
        if num==1:
            count+=1
            max_count=max(max_count,count)
        else:
            count=0
    return max_count
print(max_consecutive_ones([1,1,0,1,1,1]))      # 3
print(max_consecutive_ones([1,0,1,1,0,1]))      # 2
print(max_consecutive_ones([0,0,0]))            # 0
print(max_consecutive_ones([1,1,1,1]))          # 4
print(max_consecutive_ones([]))                 # 0