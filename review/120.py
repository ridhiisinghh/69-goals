def write_AP(a_1,d,n):
    f = open("out.txt","w")
    term = a_1
    for i in range(0,n):
        f.write(str(term))
        f.write(" ")
        term += d
    f.close()
    L = open("out.txt","r")
    read = L.read()
    print(read)
    L.close()
write_AP(21,3,6)