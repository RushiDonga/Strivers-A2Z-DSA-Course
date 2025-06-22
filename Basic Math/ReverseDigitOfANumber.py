# Brute Force
number = int(input("Number: "))
rev = 0
while number > 0:
    digit = int(number % 10)
    rev = rev * 10 + digit
    number = number // 10

print(str(rev))

# Optimal Solution
# Brut Force is the Optimal Solution