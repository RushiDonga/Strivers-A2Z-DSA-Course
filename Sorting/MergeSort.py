def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left=left+1
        else:
            temp.append(arr[right])
            right=right+1

    while left <= mid:
        temp.append(arr[left])
        left=left+1

    while right <= high:
        temp.append(arr[right])
        right=right+1

    print(temp)

    for i in range(low, high+1):
        arr[i] = temp[i-low]

def mergeSort(arr, low, high):
    if low >= high:
        return
    
    mid = int((low+high)/2)
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

mergeSort(arr, 0, len(arr)-1)
print(arr)

