def freq_to_words(words):
    d1 ={}
    for i in range(0,len(words)):
        if(words[i] not in d1):
            d1[words[i]] = 1
        else:
            d1[words[i]] += 1
    L1 = d1.values()
    keys = d1.keys()
    print(L1)
    dict1 = {}
    for i in L1:
        L2 = []
        for key in keys:
            if(d1.get(key) == i):
                L2.append(key)
        dict1[i] = L2
    return dict1
print(freq_to_words(['a','random','collection','a','random','another','a']))
