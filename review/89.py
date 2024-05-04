def factors(n):
    set1 = {1}
    for i in range(2,n+1):
        if(n%i==0):
            set1.add(i)
    return set1
print(factors(9))

def common_factors(a,b):
    set_a = factors(a)
    set_b = factors(b)
    set1 = set_a.intersection(set_b)
    return set1
print(common_factors(27,81))

def factors_upto(n):
    D = {}
    for i in range(1,n+1):
        D[i] = factors(i)
    return D
print(factors_upto(8))
    
