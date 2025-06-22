import math

num = int(input("Number: "))
arr = []
x = num

while x > math.sqrt(num):
    if num % x == 0:
        arr.append(x)
        arr.append(int(num/x))

    x = x-1

if(len(arr) == 2):
    print(True)
else:
    print(False)