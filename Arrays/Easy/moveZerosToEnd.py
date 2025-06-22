def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def moveZerosToEnd(arr):
    i = 0
    j = 0
    while j < len(arr):
        if i == j:
            i=i+1
            j=j+1

        if arr[j] == 0:
            j=j+1
            continue

        if i < j:
            swapElements(arr, i, j)
            i=i+1
            j=j+1      

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

moveZerosToEnd(arr)
print("Zeros at end: ", arr)