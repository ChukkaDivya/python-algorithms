def is_sorted(arr):
    ascending = True
    descending = True

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            ascending=False
        if arr[i]<arr[i+1]:
            descending=False
    if ascending:
        return "Array sorted in ascending order"
    elif descending:
        return "Array sorted in descending order"
    else:
        return "Array is not already sorted"
# Test Cases
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([5, 4, 3, 2, 1]))
print(is_sorted([1, 3, 2, 4]))