print("Enter first integer")
a = int(input())
print("Enter second integer")
b= int(input())
print("Enter third integer")
c = int(input())
print("Enter fourth integer")
d= int(input())
list = [a,b,c,d]
list.sort()
for i in range(0,3):
    print(list[i], end=" ")
print(list[3])

