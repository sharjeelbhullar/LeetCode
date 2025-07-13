def printNto1(i, n):
    if i < n:
        return
    print(i, end=" ")
    printNto1(i-1, n)

n = int(input("Enter a number: "))
printNto1(n, 1)