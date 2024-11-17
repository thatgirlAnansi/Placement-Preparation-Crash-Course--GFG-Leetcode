def printNos(n):
    if n > 0:
        printNos(n - 1)
        print(n, end=' ')


# Driver code
n = 10
printNos(n)
