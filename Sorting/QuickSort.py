def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while pivot >= arr[i] and i <= high-1:
            i=i+1

        while pivot < arr[j] and j >= low+1:
            j=j-1

        if i<j:
            swapElements(arr, i, j)

    swapElements(arr, low, j)
    return j

def quickSort(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)

        quickSort(arr, low, pIndex-1)
        quickSort(arr, pIndex+1, high)


n = int(input("Number of Elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Original Array: ", arr)
quickSort(arr, 0, len(arr)-1)
print("Sorted Array: ", arr)