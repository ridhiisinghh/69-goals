def std_dev(x):
    sum = 0
    n = len(x)
    for i in range(0,n):
        sum+= x[i]
    mean = sum/n
    sd = 0
    for i in range(0,n-1):
        sd += (x[i]-mean)**2
    return sd
print(std_dev([1,2,3,4,5]))
