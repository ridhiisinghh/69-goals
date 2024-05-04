movement = input()
count = 0
if (movement == "start"):
    count = 1
    while(movement!= "stop"):
        movement = input()
        if(movement == "up" or movement == "down"):
            count += 1
        else:
            count += 0
print(count)
