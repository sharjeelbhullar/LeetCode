def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

arr = [7,6,5,5,3,2,4,0,5,2,1,8,0,9,7,9,6]
insertionSort(arr)
print(arr)