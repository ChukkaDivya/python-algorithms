def array_rotation_right(arr,k):
    n=len(arr)
    if n==0:
        return arr
    k=k%n
    def reverse_array(left,right):
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    reverse_array(0,n-1)
    reverse_array(0,k-1)
    reverse_array(k,n-1)
    return arr
print(array_rotation_right([1, 2, 3, 4, 5],7))
