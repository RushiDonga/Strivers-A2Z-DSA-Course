import math

num = int(input("Number: "))
dup = num
arm = 0
len = int(math.log10(num)+1)

while dup > 0:
    digit = int(dup % 10)
    arm = arm + pow(digit, len)
    dup = dup // 10

print(num == arm)