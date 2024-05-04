name = eval(input())
date = eval(input())
if(len(name)==len(date)):
    dictionary = {}
    for i in range(0,len(name)):
        dictionary[name[i]] = date[i]
else:
    print("Members are extra or missing")
common = []
for i in range(0,len(dictionary)):
    pair = [name[i]]
    for j in range(i+1,len(dictionary)):
        if(dictionary.get(i)==dictionary.get(j)):
            pair.append(name[j])
    if(len(pair)==2):
        pair.sort()
        common.append(pair)
print(common)
            
