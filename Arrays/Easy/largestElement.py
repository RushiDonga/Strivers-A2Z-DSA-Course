def getLargestElement(arr, largest, i):
    if i >= len(arr):
        return largest
    
    if arr[i] > largest:
        print(largest)
        largest = arr[i]

    return getLargestElement(arr, largest, i+1)

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Largest Element: ", getLargestElement(arr, arr[0], 0))
