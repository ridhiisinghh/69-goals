AR1 = int(input())
AW1 = int(input())
AR2 = int(input())
AW2 = int(input())
BR1 = int(input())
BW1 = int(input())
BR2 = int(input())
BW2 = int(input())
if ( AR1>BR1 and AR2 > BR2 and  BW2==10):
     print("A WINNER")
elif (BR1>AR1 and BR2> AR2):
     print("B WINNER")
elif ( BR1==AR1 and BR2==AR2) and Bw2!= 10 ):
     print("Draw")
else:
     print("Game is on")
