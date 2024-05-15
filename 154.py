def survival(T):
    x = int(input("Enter the x coordinate"))
    y = int(input("Enter the y coordinate"))
    temp = 30 + (x**2) + (y**2) - (3*x) - (4*y)
    if(temp<T):
        return True
    else:
        return False
print(survival(36))
    