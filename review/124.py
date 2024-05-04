def get_freq(filename):
    f = open(filename, 'r')
    L = f.readlines()
    dict1 = {}
    for key in range(0,len(L)):
        L[key] = L[key].rstrip("\n")
        if(L[key] not in dict1):
            dict1[L[key]] = 1
        else:
            dict1[L[key]] += 1
    print(dict1)
    f.close()
get_freq("public_1.txt")    

