def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubbleSort(arr):
    for i in range(len(arr), -1, -1):
        temp=0
        for j in range(1, i):
            if arr[temp] > arr[j]:
                swapElements(arr, temp, j)
            temp=temp+1


n = int(input("Number fo elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element: " + str(i+1) + ": ")))

print("Original Array: ", arr)
bubbleSort(arr)
print("Sorted Array: ", arr)
