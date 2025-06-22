def getArrRev(arr, revArr = []):
    if(len(arr) < 1):
        return revArr
    element = arr.pop()
    revArr.append(element)
    return getArrRev(arr, revArr)

arrLen = int(input("Array Length: "))
arr = []
for _ in range(arrLen):
    arr.append(int(input("Element: " + str(_+1) + ": ")))

print(getArrRev(arr))