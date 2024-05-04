a = input()
b = input()
c = a+b
list = []
for i in range(0,len(c)):
    list.append(c[i])
list.sort()
sort = ""
for i in range(0,len(list)):
    sort = sort + list[i]
print(sort)
