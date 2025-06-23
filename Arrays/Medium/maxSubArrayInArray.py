def getMaxSubArray(arr):
    sum = 0
    temp = 0
    x=0
    y=0
    for i in range(len(arr)):
        temp += arr[i]
        if temp < 0:
            temp = 0
            x=i+1

        if temp > sum:
            sum = temp
            y=i

    print("Sub Array: ", arr[x:y+1])

    return sum

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Max Sum: ", getMaxSubArray(arr))