n = int(input("Enter the dimension"))
matrix1 = []
matrix2 = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input("numbers")))
    matrix1.append(a)
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input("num")))
    matrix2.append(b)
sum = []
for i in range(n):
    c = []
    for j in range(n):
        c.append(0)
    matrix2.append(c)
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        sum[i][j] = matrix1[i][j] + matrix2[i][j]
for i in sum:
    print(i)
