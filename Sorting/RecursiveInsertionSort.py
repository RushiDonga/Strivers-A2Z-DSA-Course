def swapElement(arr, i, j):
    temp = arr[i]
    arr[i]= arr[j]
    arr[j] = temp

def recursiveInsertionSort(arr, i=0):
    if i == len(arr):
        return
    
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            swapElement(arr, j, j-1)
        else:
            break

    recursiveInsertionSort(arr, i+1)


n = int(input("Number of Elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Number " + str(i+1) + ": ")))

print("Original Array: ", arr)
recursiveInsertionSort(arr)
print("Sorted Array: ", arr)
