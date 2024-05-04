def multipy(a,b):
    if(b==0):
        return 0
    else:
        sum = a +  multipy(a,b-1)
    return sum
print(multipy(4,5))