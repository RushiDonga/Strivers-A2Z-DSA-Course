def unionOfTwoSortedArrays(arr1, arr2):
    i = 0
    j = 0
    union = []

    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] < arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            
            i=i+1
        elif arr1[i] > arr2[j]:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            
            j=j+1
        else:
            j=j+1

    while i < len(arr1):
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i=i+1

    while j < len(arr2):
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j=j+1


    return union

n = int(input("Number of Elements in Array 1: "))
arr1 = []
for i in range(n):
    arr1.append(int(input("Element " + str(i+1) + ": ")))

m = int(input("Number of Elements in array 2: "))
arr2 = []
for i in range(m):
    arr2.append(int(input("Element " + str(i+1) + ": ")))

print(unionOfTwoSortedArrays(arr1, arr2))