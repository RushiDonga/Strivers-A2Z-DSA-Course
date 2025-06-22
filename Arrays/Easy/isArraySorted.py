def isArraySorted(arr, i, j):

    if j == len(arr):
        return True

    if arr[i] > arr[j]:
        return False
    
    return isArraySorted(arr, i+1, j+1)


n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Is Array Sorted:", isArraySorted(arr, 0, 1))