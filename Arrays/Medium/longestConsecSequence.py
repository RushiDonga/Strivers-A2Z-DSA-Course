def getLongestConsecutiveSeq(arr):
    count = 0
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])

    for i in range(len(arr)):
        if arr[i]-1 not in st:
            num = arr[i]
            ct = 0
            while num in st:
                ct += 1
                num += 1

            if ct > count:
                count = ct

    return count

n = int(input("Number of Elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Element " + str(i+1) + ": ")))

print(getLongestConsecutiveSeq(arr))