def is_perfect(n):
    L = []
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            L.append(i)
    for i in L:
        sum += i
    if (sum==n):
        print("perfect number")
    else:
        print("Not a perfect number")

is_perfect(7)
