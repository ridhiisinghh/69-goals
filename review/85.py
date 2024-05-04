def value_to_keys(D,value):
    list = []
    for i in D.keys():
        if(D[i]==value):
            list.append(i)  
    print(list)
value_to_keys({"ridhi":8,"adya":5,"subbu":8},2)
