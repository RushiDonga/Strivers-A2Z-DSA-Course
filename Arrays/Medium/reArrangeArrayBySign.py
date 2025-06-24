def swapElements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def displaceElement(arr, i, j):
    if i >= j:
        return
    swapElements(arr, i, j-1)
    displaceElement(arr, i+1, j-1)
    
    swapElements(arr, i, j)
    displaceElement(arr, i+1, j-1)


def reArrangeArray(arr):
    i = 0
    j = 0
    temp = 1

    while i < len(arr):
        if temp == 1:
            if arr[i] >= 0:
                i += 1
                j = i
                temp = -temp
            else:
                j += 1
                if arr[j] >= 0:
                    displaceElement(arr, i, j)
                    i += 1
                    temp = -temp
        else:
            if arr[i] < 0:
                i += 1
                j = i
                temp = -temp
            else:
                j += 1
                if arr[j] < 0:
                    displaceElement(arr, i, j)
                    i += 1
                    temp = -temp

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

reArrangeArray(arr)
print(arr)