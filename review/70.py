n = int(input("no. of points"))
list= []
for i in range(0,n):
    cord = eval(input())
    list.append(cord)
p = eval(input())
dist = {}
for i in range(0,n):
    distance = (list[i][0] - p[0])**2  +  (list[i][1] - p[1])**2 
    dist[list[i]] = distance
print(dist)
    
