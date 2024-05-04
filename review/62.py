n = int(input("enter the size"))
matrix = []
for i in range(1,n+1):
    a =[]
    for j in range(1,n+1):
        if(i==j):
            a.append(1)
        else:
            a.append(0)
    matrix.append(a)
print(matrix)
