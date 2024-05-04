def is_magic(mat):
    sumd1 = 0
    sumd2 = 0
    for i in range(0,len(mat)):
        sumd1 += mat[i][i]
        sumd2 += mat[i][len(mat)-i-1]
    if(sumd1!=sumd2):
        return False
    else:
        for i in range(0,len(mat)):
            sumr = 0
            sumc = 0
            for j in range(0,len(mat[i])):
                sumr += mat[i][j]
                sumc += mat[j][i]
        if(sumr == sumc == sumd1):
            return True
        else:
            return False
print(is_magic([[1,1,1],[1,1,1],[1,1,4]]))
