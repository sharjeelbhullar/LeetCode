def reverse_array(l, r, arr):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse_array(l+1, r-1, arr)

arr = [7,6,5,4,3,2,1]
reverse_array(0, len(arr)-1, arr)
print(arr)
    