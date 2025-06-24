import sys

def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Implementation of Merge Sort
def mergeSort(arr, left, right):
    if left >= right:
        return
    pIndex = int((left+right)/2)
    mergeSort(arr, left, pIndex)
    mergeSort(arr, pIndex+1, right)
    merge(arr, left, pIndex, right)

def merge(arr, low, mid, right):
    i = low
    j = mid+1
    temp = []

    while i<=mid and j<=right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for i in range(low, right+1):
        arr[i] = temp[i-low]

def getSmallestIndex(arr, i):
    diff = sys.maxsize
    index = i

    for x in range(i+1, len(arr)):
        if arr[x] > arr[i] and arr[x]-arr[i]<diff:
            diff = arr[x]-arr[i]
            index = x

    return index

def getBreakPoint(arr):
    i = len(arr)-2
    while i >= 0:
        if arr[i] < arr[i+1]:
            return i
        
        i -= 1
        
    return -1

def getNextPermutation(arr):
    breakPoint = getBreakPoint(arr)
    if breakPoint == -1:
        mergeSort(arr, 0, len(arr)-1)
        return

    swapElements(arr, breakPoint, getSmallestIndex(arr, breakPoint))
    mergeSort(arr, breakPoint+1, len(arr)-1)

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))
    
getNextPermutation(arr)
print(arr)

# Time Complexity: O(3N); finding the breakPoint, finding the smallest Element, reversing the array all of them takes time=O(N)
# Space Complexity: O(1)