def rotation(L):
    L1 = []
    L1.append(L[-1])
    for i in range(0,len(L)-1):
        L1.append(L[i])
    return L1
def clockwise_rot(n,L):
    if(n==0):
        return L
    else:
        L1 = rotation(L)
        return clockwise_rot(n-1,L1)
        
n = int(input("Enter the no of rotation"))
L = [1,2,3,4,5]
print(clockwise_rot(n,L))