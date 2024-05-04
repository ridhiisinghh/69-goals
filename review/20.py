n = int(input())
x= int(input())
if(x<n):
   y = int(input())
else:
   print('invalid input of x')
if((x+y)<n):
   z = int(input())
else:
   print('invalid input of y')
if((x+y+z)==n and (x!=0 or y!=0 or z!=0) and (x!=y!=z) ):
     print('fair')
else:
     print('unfair')
