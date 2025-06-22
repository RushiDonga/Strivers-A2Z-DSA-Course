def getFibonacci(n, i=0, j=1):
    print(str(i))
    if j > n:
        return
    getFibonacci(n, j, j+i)

n = int(input("Number: "))
getFibonacci(n)
