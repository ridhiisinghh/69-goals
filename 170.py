box1 =[]
box2 =[]
box3 =[]
box4 =[]
box5 =[]
boxes = [box1,box2,box3,box4,box5]
value = input()
for i in range(1,len(value)):
    boxes[i%5].append(int(value[i]))
max = 0
for i in range(0,len(boxes)):
    if(sum(boxes[i])>max):
        max = sum(boxes[i])
print(max)
for i in range(0,len(boxes)):
    if(sum(boxes[i])==max):
        print(boxes[i])
        break

    

