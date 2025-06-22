def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def recursiveBubbleSort(arr, i):
    if i == 0:
        return 
    
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            swapElements(arr, j, j+1)

    recursiveBubbleSort(arr, i-1)


n = int(input("Number of Elements: "))
arr = []
    
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Original Array: ", arr)
recursiveBubbleSort(arr, len(arr)-1)
print("Sorted Array: ", arr)
