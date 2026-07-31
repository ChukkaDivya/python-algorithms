# Problem Statement
# Given an unsorted array of integers, find the length of the longest consecutive sequence.
# The numbers in the sequence do not need to be adjacent in the array, only consecutive in value.
# Your algorithm should run in O(n) time.
def longest_consecutive(nums):
    if not nums:
        return 0
    num_set=set(nums)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            current=num
            length=1
            while current+1 in num_set:
                current+=1
                length+=1
            longest=max(longest,length)
    return longest
print(longest_consecutive([100,4,200,1,3,2]))      # 4
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))  # 9
print(longest_consecutive([1,2,0,1]))              # 3
print(longest_consecutive([]))                     # 0
print(longest_consecutive([10]))                   # 1