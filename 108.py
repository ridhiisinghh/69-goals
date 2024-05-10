def uniq(L):
    if(len(L)==0):
        return L
    if(L[-1] not in L[:-1]):
        return uniq(L[:-1])+ L[-1]
    else:
        return uniq(L[:-1])
print(uniq([1,3,5,7,3,9]))
    