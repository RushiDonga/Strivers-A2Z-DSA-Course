def findMissingNumber(arr):
    x = 1
    for i in range(len(arr)):
        if arr[i] == x:
            x=x+1
        else:
            return x

n = int(input("Number of Elements: "))
arr = []
for i in range(n-1):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Missing Number: ", findMissingNumber(arr))