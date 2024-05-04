number = input("call me in ")
count = 0
if(number[0] != 6 or number[0] != 7 or number[0] != 8 or number[0] != 9):
    print("in")
else:
    if(len(number)!= 10):
        print("invalid")
    else:
        for i in range(0,10):
           x = number[i]
           for j in range(i,10):
                if(number[j]==x):
                    count += 1
                    if(count<7):
                         print("valid")
                    else:
                         print("invalid")            
