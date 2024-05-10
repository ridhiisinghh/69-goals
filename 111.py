def linear(P,Q,k):
    if(len(P)==len(Q)==0):
        return True
    if(len(P)!=len(Q) and P[-1]!=k*Q[-1]):
        return False
    else:
        return linear(P[:-1],Q[:-1],k)
print(linear([1,2,3],[2,4,6],3))