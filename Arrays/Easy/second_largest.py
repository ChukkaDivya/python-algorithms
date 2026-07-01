def second_largest(arr):
    if len(arr)<2:
        return -1
    largest=arr[0]
    second=float('-inf')
    for i in range(1,len(arr)):
        if arr[i]>largest:
            second=largest
            largest=arr[i]
        elif arr[i]>second and arr[i]!=largest:
            second=arr[i]
    return second if second!=float('inf') else -1
nums1 = [12, 35, 1, 10, 34, 1]      # Expected: 34
nums2 = [10, 10, 10]                # Expected: -1
nums3 = [-5, -2, -8, -1]            # Expected: -2
nums4 = [5]                         # Expected: -1
print(second_largest(nums1))
print(second_largest(nums2))
print(second_largest(nums3))
print(second_largest(nums4))