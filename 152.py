def primes_galore(L):
    count = 0
    for i in range(1,len(L)):
        cnt = 0
        for j in range(1,len(L)):
            if(i%j==0):
                cnt+=1
        if(cnt>2):
            v=0
            for k in range(1,len(L)):
                if(L[i]%i):
                    v+=1
            if(v>2):
                count+=1
    return count
print(primes_galore([1,3,11,18,17,23,6,8,10]))            


