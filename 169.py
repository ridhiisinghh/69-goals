def count(d1):
    cnt = 0
    for i in d1:
        if(d1[i] == True):
            cnt+=1
    return cnt
def exactly_two(players):
    set = {1}
    for i in players:
        if(count(players.get(i)) == 2):
            set.add(i)
    set.remove(1)
    return set
print(exactly_two({'karthik':{'tennis':True,'bad':True,'cricket':False} ,'rahul':{'tennis':False,'bad':True,'cricket':False} }))