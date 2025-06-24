def getLeader(arr):
    largest = arr[len(arr)-1]
    print(largest)
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1] and arr[i] > largest:
            print(arr[i])
            largest = arr[i]

n = int(input("Number of Elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

getLeader(arr)