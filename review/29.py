string = input()
list =[]
vowels = ['a','e','i','o','u']
for i in range(0,len(string)):
    list.append(string[i])
if ('a' in list and 'e' in list and 'i' in list and 'o' in list and 'u' in list):
    print(vowels)
else:
    print("none")
