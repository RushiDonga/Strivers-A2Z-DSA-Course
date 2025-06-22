arr = [10, 5, 10, 15, 10, 5]
dict = {}

for i in range(len(arr)):
    if dict.get(arr[i]) == None:
        dict.update({arr[i]: 1})
    else:
        dict.update({arr[i]: dict.get(arr[i])+1})

maxFreq = 0
minFreq = len(arr)
maxEle = 0
minEle = 0

for x, y in dict.items():
    # Max Frequency
    if maxFreq < y:
        maxFreq = y
        maxEle = x

    if minFreq > y:
        minFreq = y
        minEle = x

print("Highest Frequency: " + str(maxEle))
print("Lowest Frequency: " + str(minEle))
