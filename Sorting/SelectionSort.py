def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selectionSort(arr):
    j = 0
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j

        swapElements(arr, min, i)

n = int(input("Number of Elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Original Array: ", arr)
selectionSort(arr)
print("Sorted Array: ", arr)
