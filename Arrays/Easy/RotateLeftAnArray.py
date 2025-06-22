def swapElements(arr):
    temp = arr[0]
    arr[0] = arr[1]
    arr[1] = temp

def rotateByOne(arr, temp, i, j):

    if j>len(arr) and i==len(arr):
        arr[i-1] = temp
        return
    elif j >= len(arr):
        arr[i-1] = arr[i]
        arr[i] = temp
        return
        
    arr[i-1] = arr[i]
    arr[j-1] = arr[j]
    rotateByOne(arr, temp, i+2, j+2)

def rotateByD(arr, rotateBy):
    rotate = rotateBy if len(arr) > rotateBy else rotateBy%len(arr)
    
    for _ in range(rotate):
        rotateByOne(arr, arr[0], 1, 2)


n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

rotateBy = int(input("Rotate Left by: "))

print("Original Array: ", arr)
rotateByD(arr, rotateBy)
print("Rotated by " + str(rotateBy) + ": ", arr)