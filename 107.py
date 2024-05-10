def non_decreasing(L):
    if(len(L)==0 or len(L)== 1 ):
        return True
    if(L[0]>L[1]):
        return False
    else:
        return non_decreasing(L[1:])

print(non_decreasing([1,2,4,9]))