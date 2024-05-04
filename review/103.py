def logarithm(x):
    if(x==1):
        return 0
    else:
        power = 1 + logarithm(x/2)
    return power
print(logarithm(32))