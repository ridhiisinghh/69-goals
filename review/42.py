n = int(input())
answer = []
for z in range(3,n):
    for y in range(2,z):
        for x in range(1,y):
            if(((x*x)+(y*y))==(z*z)):
                answer.append([x,y,z])
answer.sort()
print(answer)
