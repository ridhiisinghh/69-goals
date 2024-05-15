Seq = eval(input("Enter the sequence of integers"))
n = len(Seq)
if(n%2==0):
    left_sum = 0
    right_sum = 0
    for i in range(0,(n//2)-1):
        left_sum += Seq[i]
    for i in range(n//2,n):
        right_sum+= Seq[i]
    if(left_sum>right_sum):
        print("left-heavy")
    if(left_sum<right_sum):
        print("Right heavy")
    else:
        print("Balanced")