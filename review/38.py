print("Enter any Positive intger")
n = int(input())
summ = 0
while(n!=0):
    digit = n%10
    summ = summ+digit
    n = n//10
print(summ)    
