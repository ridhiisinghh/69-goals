s= int(input("Enter the number to be multiplied"))
n = int(input("enter the size"))
matrix = []
for i in range(1,n+1):
    a =[]
    for j in range(1,n+1):
        a.append(int(input("Num")))
    for k in range(0,len(a)):
        a[k] = s*a[k]
    matrix.append(a)
print(matrix)
