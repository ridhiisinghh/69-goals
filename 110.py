def reverse(L):
    if(len(L)== 0):
        return L
    else:
        return [L.pop()]+reverse(L)
print(reverse([1,2,3,4,5,6]))