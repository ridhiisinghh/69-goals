x = int(input("pehla number "))
y = int(input("dusra number "))
count = 0
check = 0
for i in range(1,x):
    if(x%i==0):
        count += 1
for i in range(1,y):
    if(y%i==0):
        check += 1
if(count == check == 1):
    print("upar k dono number coprime hai")
else:
    print("kuch or try kro")
