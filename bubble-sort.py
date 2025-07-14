def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1,-1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [7,6,5,5,3,2,4,0,5,2,1,8,0,9,7,9,6]
bubbleSort(arr)
print(arr)