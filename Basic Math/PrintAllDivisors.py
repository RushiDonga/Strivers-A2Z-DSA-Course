import math

num = int(input("Number: "))
x = num
arr = []

while x > math.sqrt(num):
    if num % x == 0:
        arr.append(x)
        arr.append(int(num/x))
    
    x = x-1

print(arr)