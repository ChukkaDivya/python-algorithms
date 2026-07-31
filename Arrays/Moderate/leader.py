# Problem Statement
# Given an array, return all the leaders.
# A leader is an element that is greater than all the elements to its right.
# The last element is always a leader because there are no elements to its right.
def leaders(nums):
    n=len(nums)
    max_element=float('-inf')
    leaders_array=[]
    for i in range(n-1,-1,-1):
        if nums[i]>max_element:
            leaders_array.append(nums[i])
            max_element=nums[i]
    leaders_array.reverse()
    return leaders_array
print(leaders([10,22,12,3,0,6]))     # [22,12,6]
print(leaders([4,7,1,0]))            # [7,1,0]
print(leaders([5,4,3,2,1]))          # [5,4,3,2,1]
print(leaders([1,2,3]))              # [3]
print(leaders([16,17,4,3,5,2]))      # [17,5,2]