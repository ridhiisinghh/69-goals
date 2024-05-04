filename = "public_1.txt"
def read_line(filename,n):
    f = open(filename,"r")
    Lines = f.readlines()
    if(len(Lines)>n):
        print(Lines[n])
    else:
        print("None")
    f.close()

read_line(filename,2)