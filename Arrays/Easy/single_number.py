def single_number(nums):
    xor=0
    for num in nums:
        xor^=num
    return xor
print(single_number([2,2,1]))          # 1
print(single_number([4,1,2,1,2]))      # 4
print(single_number([1]))              # 1
print(single_number([7,3,5,3,5]))      # 7