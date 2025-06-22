def linearSearch(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
        
    return -1

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

ele = int(input("Search Element: "))
print("Element Present at index: ", linearSearch(arr, ele))