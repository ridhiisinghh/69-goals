import csv
def number_grid(m,n):
    f = open("numgrid.csv",'w')
    writer = csv.writer(f)
    k = 1
    List1 = []
    for i in range(1,m+1):
        L = []
        for j in range(1,n+1):
            L.append(k)
            k += 1
        List1.append(L)
    print(List1)
    f.close()
    # new = open("numgrid.csv",'r')
    # read = csv.reader(ff)
    # for row in read:
    #     print(row)
    # new.close()
