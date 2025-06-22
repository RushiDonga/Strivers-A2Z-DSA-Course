def getSum(n, sum=0):
    if n < 1:
        return sum
    return getSum(n-1, sum+n)

num = int(input("Number: "))
print(getSum(num))