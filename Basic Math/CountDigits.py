# My Solution
# number = int(input("Number: "))
# count = 0
# while(number > 0):
#     count=count+1
#     number=number // 10

# print("Number Length: " + str(count))

#  Optimized Solution
import math 

num = int(input("Number: "))
count = int(math.log10(num) + 1)
print("Num Length: " + str(count))