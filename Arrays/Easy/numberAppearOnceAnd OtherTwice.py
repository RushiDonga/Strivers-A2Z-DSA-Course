def numberThatAppearOnce(arr):
    xor = 0
    for i in range(len(arr)):
        xor ^= arr[i]

    return xor


n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print("Number that appear Once: ", numberThatAppearOnce(arr))
