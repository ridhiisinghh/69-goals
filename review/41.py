n = int(input("Enter the number"))
list = [1]
count = 0
for i in range(2,n):
    for j in range(1,i+1):
        if(i%j==0):
            count = count+1
    if(count<=2):
        list.append(i)
list.append(n)
print(list)
if(len(list)>2):
    print(sum(list))
else:
    print('0')
