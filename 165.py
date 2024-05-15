def exact_count(para,n):
    L= para.split(" ")
    dict = {}
    for i in range(0,len(L)):
        if(L[i] not in dict):
            dict[L[i]] = 1
        else:
            dict[L[i]]+=1
    val = dict.values()
    if(n in val):
        return True
    else:
        return False
print(exact_count("the string has no other special characters other than the space",2))