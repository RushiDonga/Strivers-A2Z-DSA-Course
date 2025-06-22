def getMajorityElement(arr):
    count = 0
    element = 0
    for i in range(len(arr)):
        if count == 0:
            count += 1
            element = arr[i]

        if arr[i] != element:
            count -= 1

    return element

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Majority Element: ", getMajorityElement(arr))

# Time Complexity: O(N); N = size of array. We are just iterating one through the array
# Space Complexity: O(1); we are using constant space