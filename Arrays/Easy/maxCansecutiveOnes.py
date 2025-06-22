def findMaxConsecutiveOnes(arr):
    max = 0
    temp = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            temp += 1
        else:
            temp = 0
        
        if temp > max:
            max = temp

    return max


n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Maximum Consecutive Ones: ", findMaxConsecutiveOnes(arr))

# Time Complexity: O(N); N = Size of Array
# Space Complexity: O(1); No extra space is used