print("Enter any number")
a= int(input())
print("Enter any number")
b= int(input())
sum = 0;
for i in range(1000,2001):
    if(i%a==0 and i%b==0):
        sum = sum+i
print(sum)
