string = input("enter any word")
string.lower()
list = []
for i in range(0,len(string)):
    list.append(string[i])
list.sort()
new_str = ''
for i in range(0,len(list)):
    new_str += list[i]
print(new_str)
