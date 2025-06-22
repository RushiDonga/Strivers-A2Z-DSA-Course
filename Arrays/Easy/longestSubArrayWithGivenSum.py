def getLongestSubArrayWithGivenSum(arr, sum):
    i = 0
    j = i+1
    temp = arr[i]
    steps = 0
    
    while i<len(arr)-1:
        temp += arr[j]
        if temp < sum:
            if j == len(arr)-1:
                i += 1
                j = i+1
            else:
                j += 1
            continue

        if temp == sum and steps < j-i+1:
            steps = j-i+1
            temp += sum

        if temp > sum:
            i += 1
            j = i+1
            temp = arr[i]

    return steps

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

sum = int(input("Sum: "))
print("Longest SubArray with sum=" + str(sum) + " is of length: ", str(getLongestSubArrayWithGivenSum(arr, sum)))