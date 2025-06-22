def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid+1

    while i<=mid and j<=right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i<=mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1
    
    for i in range(left, right+1):
        arr[i] = temp[i-left]

def mergeSort(arr, left, right):
    if left >= right:
        return
    
    pIndex = int((left+right)/2)
    mergeSort(arr, left, pIndex)
    mergeSort(arr, pIndex+1, right)
    merge(arr, left, pIndex, right)


def variant1(arr, sum):
    mergeSort(arr, 0, len(arr)-1)
    i=0
    j=len(arr)-1

    while i<j:
        tempSum = arr[i] + arr[j]
        if tempSum == sum:
            return "YES"
        elif tempSum < sum:
            i += 1
        else:
            j -= 1

    return "NO"

def variant2(arr, sum):
    mergeSort(arr, 0, len(arr)-1)
    i=0
    j=len(arr)-1

    while i<j:
        tempSum = arr[i] + arr[j]
        if tempSum == sum:
            return [i, j]
        elif tempSum < sum:
            i += 1
        else:
            j -= 1

    return [-1, -1]


n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

sum = int(input("Sum: "))

print("Pair Exists: ", variant1(arr, sum))
print("Indexes: ", variant2(arr, sum))