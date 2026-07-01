def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
nums1 = [1, 2, 3, 4, 5]      # True
nums2 = [1, 2, 2, 3, 4]      # True
nums3 = [1, 3, 2, 4]         # False
nums4 = [5]                  # True
nums5 = [5, 4]               # False
print(is_sorted(nums1))
print(is_sorted(nums2))
print(is_sorted(nums3))
print(is_sorted(nums4))
print(is_sorted(nums5))