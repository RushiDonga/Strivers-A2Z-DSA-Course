def removeDuplicates(arr, i, j):

    if j == len(arr):
        return
    
    if(arr[i] == arr[j]):
        del arr[i]
        i=i-1
        j=j-1
    
    removeDuplicates(arr, i+1, j+1)
    

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Original Array: ", arr)
removeDuplicates(arr, 0, 1)
print(arr)