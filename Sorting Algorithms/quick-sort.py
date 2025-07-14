def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high-1 and arr[i] <= pivot:
            i += 1

        while j >= low+1 and arr[j] > pivot: 
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[low] = arr[low], arr[j]
    return j

def quickSort(arr, low, high):
    if low < high:
        pindex = partition(arr, low, high)
        quickSort(arr, low, pindex-1)
        quickSort(arr, pindex+1, high)

arr = [7,6,5,5,3,2,4,0,5,2,1,8,0,9,7,9,6]
quickSort(arr, 0, len(arr)-1)
print(arr)