n = int(input())
count = 0
list = []
for i in range(1,n):
    if(n%i==0):
        for j in range(1,i):
            if(i%j==0):
                count += 1
        if(count<=2):
            list.append(i)
print(list)
