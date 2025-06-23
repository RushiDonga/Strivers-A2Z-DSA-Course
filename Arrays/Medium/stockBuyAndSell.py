def getMaxProfit(arr):
    min = arr[0]
    maxPro = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]

        if arr[i] - min > maxPro:
            maxPro = arr[i] - min

    return maxPro

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Max Profit: ", getMaxProfit(arr))

# Time Complexity: O(N); N = size of the array
# Space Complexity: O(N) because it uses constant space
