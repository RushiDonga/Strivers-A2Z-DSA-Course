def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sortArrayOd012(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while mid < high:
        if arr[mid] == 0:
            swapElements(arr, low, mid)
            low += 1
            mid += 1
        
        if arr[mid] == 2:
            swapElements(arr, mid, high)
            high -= 1

        if arr[mid] == 1:
            mid += 1

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

sortArrayOd012(arr)
print("Sorted Array: ", arr)

# Time Complexity: O(N); N = size of Array
# Space Complexity: O(1); it uses constant space