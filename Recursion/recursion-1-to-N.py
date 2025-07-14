def printNtime(i, n):
    if i > n:
        return
    print(i, end=" ")
    printNtime(i+1, n)

n = int(input("Enter a number: "))
printNtime(1, n)