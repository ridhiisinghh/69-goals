#Q.no 7
Sum = 0
print('Enter the number of 5 digit')
Num= int(input())
while(Num != 0):
    Sum = Sum + Num%10
    Num = Num//10    
print('Sum =', Sum)


# Q.no10
print('Enter the number plate')
Num_plate = input()
visible = 'TN07'
if(Num_plate[0:4] == visible):
    print('True')
elif(Num_plate[4:8]== visible):
     print('True')
else:
    print('False')

# Q.no9
print('Enter the roll number')
Roll_no = input()
Branch = 'DS'
if(Roll_no[0:2] == Branch):
    print('Student belongs to data science')
else:
    print('Student does not belongs to data science')


# Q.no1
list = [1,2,3,4,5]
for i in range(0,5):
    print(list[i])

# Q.no2
for i in range(0,5):
    for j in range(0,i+1):
        print('*',end = '')
    print('')


# Q no. 3
print('Enter the number ')
x = int( input())
print("square of the number is :", x*x) 


# Q.no5
print('Enter the first name')
f_name = input()
print('Enter the last name')
l_name = input()
print (f_name + " " + l_name)


# Q.no4
print('Enter the first number ', end = '')
num1 = int(input())
print('Enter the second number ', end = '')
num2 = int(input())
print('sum is ', num1 + num2)

# Q.no6
print('Enter the vehicle number')
vehicle_num = input()
print(vehicle_num[0:4])


