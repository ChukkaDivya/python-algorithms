def two_sum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in hashmap:
            return[hashmap[complement],i]
        hashmap[nums[i]]=i
print(two_sum([2,7,11,15], 9))      # [0,1]
print(two_sum([3,2,4], 6))          # [1,2]
print(two_sum([3,3], 6))            # [0,1]
print(two_sum([1,5,3,7], 8))        # [1,2]