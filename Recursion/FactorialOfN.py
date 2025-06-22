def getFactorial(n, fac=1):
    if n < 1:
        return fac
    return getFactorial(n-1, fac*n)

num = int(input("Number: "))
print(getFactorial(num))