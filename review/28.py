E1 = int(input())
E2 = int(input())
E3 = int(input())
E4 = int(input())
E5 = int(input())
if((E1+E2)%2==0 and (E2+E3)%2==0 and (E3+E4)%2==0 and (E4+E5)%2==0 and (E5+E1)%2==0 ):
      print("Meeting helded")
else:
      print("Meeting cancelled")
