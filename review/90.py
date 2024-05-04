list1 = eval(input())
real_dict = {}
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for char in alpha:
    list2 = []
    for i in range(0,len(list1)):
        if(list1[i][0] == char):
            list2.append(list1[i])
    real_dict[char] = list2
print(real_dict)
