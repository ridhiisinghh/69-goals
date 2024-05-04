def get_row(mat,row):
    return mat[row]
print(get_row([[1,2,3],[4,5,6],[2,4,7]],1))


def get_column(mat,col):
    L = []
    for i in range(0,len(mat)):
        L.append(mat[i][col])
    return L

print(get_column([[1,2,3],[4,5,6],[2,4,7]],1))
