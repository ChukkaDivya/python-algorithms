# Merge Two Sorted Arrays
# Problem : You are given two sorted arrays. Merge them so the combined elements are in sorted order.
def merge_sorted_arrays(arr1,arr2):
    i=0
    j=0
    result=[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i]<=arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    while i<len(arr1):
        result.append(arr1[i])
        i+=1
    while j<len(arr2):
        result.append(arr2[j])
        j+=1
    return result
print(merge_sorted_arrays(
    [1,3,5,7],
    [2,4,6,8]
))
print(merge_sorted_arrays(
    [1,2,2,5],
    [2,3,6]
))
print(merge_sorted_arrays([], [1,2,3]))