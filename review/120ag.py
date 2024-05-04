def add_period(filename):
    f = open("out.txt",'w')
    exf = open(filename,'r')
    exl = exf.readlines()
    for line in exl:
        line = line.rstrip("\n")
        f.write( str(line) + str('.') + "\n")
    exf.close()
    f.close()
    read = open("out.txt",'r')
    print(read.readlines())
    read.close()

add_period("public_1.txt")