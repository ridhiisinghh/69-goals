filename = "public_1.txt"
def get_max_line(filename):
    f = open(filename,"r")
    L = f.readlines()
    Maximum = max(L)
    for i in range(0,len(L)):
        if(L[i]== Maximum):
            print(i+1)

get_max_line(filename)
