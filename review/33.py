print("Enter the number")
n = int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i , "is a factor")
    else:
        print(i , "is not a factor")
