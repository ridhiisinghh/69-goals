list = []
num = int(input())
for i in range(0,num):
    x = input()
    list.append(x)
list.append('abcdefghijklmnopqrstuvwxyz')
check = 26
for i in range(0,len(list)):
    count = len(list[i])
    if(count<check):
        check = count
        word = list[i]
print(word)
    
