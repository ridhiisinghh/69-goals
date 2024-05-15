def balanced(word):
    list = []
    for i in range(0,len(word)):
        if(word[i]=="{" or word[i]== "[" or word[i]== "(" or word[i]== "}" or word[i]== "]" or word[i]== ")" ):
            list.append(word[i])
    print(list)
    cnt = 0
    count = 0
    for i in range(0,len(list)):
        if(list[i]=="{" or list[i]=="[" or list[i]=="(" ):
            cnt+=1
        if(list[i]=="}" or list[i]=="]" or list[i]==")" ):
            count+=1
    print(cnt)
    print(count)
    if(count==cnt):
        for i in range(0,len(list)):    
            if((list[i]== "{" and list[i+1]== "]") or (list[i]== "{" and list[i+1]== ")") or (list[i]== "[" and list[i+1]== "}") or (list[i]== "[" and list[i+1]== ")") or (list[i]== "(" and list[i+1]== "}") or (list[i]== "(" and list[i+1]== "]")):
                return False
            else:
                return True
    else:
        return False

print(balanced("{ri[A(Q[Q)]]}"))