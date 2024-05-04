def is_empty(L):
    if(len(L)==0):
        print(True)
    else:
        print(False)
def first(L):
    if(len(L)>0):
        print(L[0])
    else:
        print(None)
def last(L):
    if(len(L)>0):
        return L[-1]
    else:
        return None
def init(L):
    if(len(L)>0):
        for i in range(0,len(L)-1):
            print(L[i],end=' ')
    else:
        print("none")
def rest(L):
    if(len(L)>0):
        for i in range(1,len(L)):
            print(L[i],end=' ')
    else:
        print("none")

first([])
init([3,5,2,7,8])
