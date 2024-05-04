def dict_to_list(D):
    print(D.items())
dict_to_list({"ridhi":2,"adya":4,"subbu sir":6})

def list_to_dict(L):
    D = {}
    keys = []
    values = []
    for i in L:
        keys.append(i[0])
        values.append(i[1])
    for i in range(0,len(keys)):
        D[keys[i]]=values[i]
    print(D)
list_to_dict([("adya",2),("ridhi",5),("subbu",7),("ridhi",7)])
