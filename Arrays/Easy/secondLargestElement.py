import sys

def getSecondLargestElement(arr):
    large = -sys.maxsize - 1
    sec_large = -sys.maxsize - 1

    for i in range(len(arr)):
        if arr[i] > large:
            sec_large = large
            large = arr[i]
        elif arr[i] > sec_large:
            sec_large = arr[i]

    return sec_large


n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Second Largest Element: ", getSecondLargestElement(arr))