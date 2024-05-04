print("Enter a positive number greater than 1")
n= int(input())
count = 0
for i in range(1,n+1):
    if(n%i==0):
        count = count+1
if(count>2):
    print("not a prime number")
else:
    print("prime number")
