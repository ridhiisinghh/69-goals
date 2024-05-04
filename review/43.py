str1 = input()
str2 = input()
list1 =[]
list2 = []
for i in range(0,len(str1)):
    list1.append(str1[i])
for i in range(0,len(str2)):
    list2.append(str2[i])
print(list1)
print(list2)
for i in range(0,len(list1)+1):
    for j in range(0,len(list2)+1):
        if(list1[i]==list2[j]):
            list2.remove(j)
list1.extend(list2)
print(list1)
