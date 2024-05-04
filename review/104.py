def palindrome(string):
    if(string[0]==string[-1]):
        return True
    else:
        palindrome(string[1:-2])
        return False
print(palindrome("vekeva"))