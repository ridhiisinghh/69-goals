s = input("Enter the Expression")
add = []
sub = []
numb = ""
flag = False
for charac in s:
    if(charac == "+" and flag == False):
        add.append(int(numb))
        print(numb)
        numb = ""
    elif(charac == "+" and flag):
        sub.append(int(numb))
        print(numb)
        numb = ""
        flag = False
    elif(charac == "-" and flag == False):
        add.append(int(numb))
        print(numb)
        numb = ""
        flag = True
    elif(charac == "-" and flag):
        sub.append(int(numb))
        print(numb)
        numb = ""
    else:
        numb += charac
if(flag):
    sub.append(int(numb))
else:
    add.append(int(numb))
print(sum(add)-sum(sub))
