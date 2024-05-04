def relation(file1,file2):
    f1 = open(file1,'r')
    f1_cont = f1.readlines()
    f2 = open(file2,'r')
    f2_cont = f2.readlines()
    if(len(f2_cont)<len(f1_cont)):
        for i in range(0,len(f2_cont)):
            if(f1_cont[i]==f2_cont[i]):
                i+=1
        print("file1 is subset of file2")
    if(len(f1_cont)==len(f2_cont)):
        for i in range(0,len(f1_cont)):
            f1_cont[i].rstrip("\n")
            f2_cont[i].rstrip("\n")
            if(f1_cont[i]==f2_cont[i]):
                i+=1
        print("file1 is equal to file2")
    f1.close()
    f2.close()
relation("public_1.txt","public_1_2.txt")