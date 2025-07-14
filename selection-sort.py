def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j

        arr[mini], arr[i] = arr[i], arr[mini]

arr = [7,6,5,5,3,2,4,0,5,2,1,8,0,9,7,9,6]
selectionSort(arr)
print(arr)