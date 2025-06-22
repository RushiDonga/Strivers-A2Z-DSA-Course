# Brut Force Solution
# n1 = int(input("Number 1: "))
# n2 = int(input("Number 2: "))

# sm = n2-1 if n1 > n2 else n1-1

# while sm > 0:
#     if n1%sm == 0 and n2%sm == 0:
#         print(sm)
#         exit()

#     sm = sm - 1

# print(int(1))

# Optimal Solution: Euclidean Algorithm
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

while n1 != n2:

    if n1 < n2:
        n2 = n2 - n1
    else:
        n1 = n1 - n2


print(n1)