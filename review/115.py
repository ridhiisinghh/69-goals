filename = "public_1.txt"
def read_file(filename):
    f = open(filename,"r")
    for x in f:
        print(x,end = "")
    f.close()
read_file(filename)