def movement(e,move,n):
    list1 = []
    list1.append(e[0])
    list1.append(e[1])
    if(move=="North"):
        if(list1[0]!=n):
            list1[0]+=1
    if(move=="South"):
        if(list1[0]!=1):
            list1[0]-=1
    if(move=="East"):
        if(list1[1]!=n):
            list1[1]+=1
    if(move=="West"):
        if(list1[1]!=1):
            list1[1]-=1
    f = (list1[0],list1[1])
    return f
def final(n,moves):
    e = (1,1)
    for i in range(0,len(moves)):
        if(e!=(n,n)):
            e = movement(e,moves[i],n)
    return e

print(final(5,["North","East","North","West","West","South"]))