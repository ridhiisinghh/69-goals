def search(L,k):
    if(len(L)==0):
        return False
    if(L[0]==k):
        return True
    else:
        return search(L[1:],k)
print(search([1,3,5,7,9],8))