def matrix_type(M):
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            if(i!=j):
                if(M[i][j]==0):
                    print("diagonal")
                else:
                    print("Non diagonal")
matrix_type([[1,0,0],[0,1,0],[0,0,1]])   