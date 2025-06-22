def checkIfPalindrome(sample, i=0):
    if i>len(sample)/2:
        return True

    if (sample[i] != sample[len(sample)-i-1]):
        return False
    return checkIfPalindrome(sample, i+1)
    

sample = str(input("Enter String: "))
print(checkIfPalindrome(sample))
