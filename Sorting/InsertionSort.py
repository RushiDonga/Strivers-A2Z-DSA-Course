def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def insertionSort(arr):
    for i in range(0, len(arr)-1):
        if arr[i+1] < arr[i]:
            index = i+1
            while(index > 0 and arr[index-1] > arr[index]):
                swapElements(arr, index, index-1)
                index=index-1
                


n = int(input("Number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Original Array: ", arr)
insertionSort(arr)
print("Sorted Array: ", arr)
