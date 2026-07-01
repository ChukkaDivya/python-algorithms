def largest_element(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest
nums = [12, 45, 7, 89, 23, 89, 5]
result=largest_element(nums)
print(result)