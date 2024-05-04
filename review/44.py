str1 = input("pehla naam:")
count = 0
for i in range(0,(len(str1)+1)//2):
    if(str1[i]!=str1[len(str1)-i-1]):
         count = 0
    else:
         count += 1
if(count == 0):
    print("Not a palindrome")
else:
    print("Palindrome")


    
