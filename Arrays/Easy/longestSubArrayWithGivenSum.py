# Optimal Solution
def getLongestSubArrayWithGivenSum(arr, k):
    dict = {}
    sum = 0
    length = 0
    for i in range(len(arr)):
        sum += arr[i]

        if sum == k:
            length = max(length, i+1)

        rem = k - sum
        if rem in dict:
            length = max(length, i-dict[rem])

        if sum not in dict:
            dict[sum] = i

    return length
# Time Complexity: O(N) or O(NlogN) in worst case; N is the length of the array
# Space Complexity: O(1); we are not using extra space



#  Not an Optimal Solution
# def getLongestSubArrayWithGivenSum(arr, sum):
#     i = 0
#     j = i+1
#     temp = arr[i]
#     steps = 0
    
#     while i<len(arr)-1:
#         temp += arr[j]
#         if temp < sum:
#             if j == len(arr)-1:
#                 i += 1
#                 j = i+1
#             else:
#                 j += 1
#             continue

#         if temp == sum and steps < j-i+1:
#             steps = j-i+1
#             temp += sum

#         if temp > sum:
#             i += 1
#             j = i+1
#             temp = arr[i]

#     return steps

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

sum = int(input("Sum: "))
print("Longest SubArray with sum=" + str(sum) + " is of length: ", str(getLongestSubArrayWithGivenSum(arr, sum)))

# Time Complexity: O(n^2); n = size of array and i-> 0 to n-1 and j->i to n-1
# Time Complexity: O(1); it uses constant Space