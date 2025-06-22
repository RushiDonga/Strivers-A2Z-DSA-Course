#  This is the Optimal Solution
number = int(input("Number: "))
duplicate = number
rev = 0

while duplicate > 0:
    digit = int(duplicate % 10)
    rev = rev*10 + digit

    duplicate = duplicate // 10

print(rev)
if number == rev:
    print(True)
else:
    print(False)