






#13 e
print('Enter the first number')
m = int(input())
print('Enter the second number')
n = int(input())
if(m<n):
    print(m)
else:
    while(m>=n):
        m = m-n
    print(m)

    



#optimum 18
#x= []
#for i in range(0,5):
#    x.append(i)
#for i in range(0,5):
  #  if(x[i-1] in x[i]):
 #       print('magical')
   # else:
    #    print('non magical')






#18
print('Enter the first number')
x1 = input()
print('Enter the second number')
x2 = input()
print('Enter the third number')
x3 = input()
print('Enter the fourth number')
x4 = input()
print('Enter the fifth number')
x5 = input()
if(x4 in x5):
    if(x3 in x4):
        if(x2 in x3):
            if (x1 in x2):
                print('magical')
else:
    print('non magical')






#17
print('Enter the word')
Word = input()
if(len(Word)%2==0):
    if(Word[-1]=='.'):
        Word.strip('.')
    else:
        Word = Word + '.'
mid = int((0+ len(Word))/2)
sub_str = Word[(mid-1): (mid+2)]
print(sub_str)



#15
print('Enter the x coordinate')
x=float(input())
print('Enter the y coordinate')
y=float(input())
if(x>0 and y>0):
    print('first quadrant')
elif(x>0 and y<0):
    print('Second quadrant')
elif(x<0 and y<0):
    print( 'Third quadrant')
elif(x>0 and y>0):
    print('Fourth quadrant')
elif(x==0 and y==0):
    print('origin')
elif(x==0 and y!=0):
    print('y-axis')
else:
    print('x-axis')


#14
print('Enter the time')
T = int(input())
if(T<0):
    print('Invalid')
elif(T<=5):
    print('Night')
elif(T<=11):
    print('Morning')
elif(T<=17):
    print('Afternoon')
elif(T<=23):
    print('Evening')
elif(T>=24):
    print('Invalid')


#13d

import math
print('Enter the first number')
x = int(input())
print('Enter the second number')
y = int(input())
power = pow(x,y)
digits = int(math.log10(power))
digits = digits+1
print(digits)







#13c
print("Enter your email ")
email_id = input()
mail_left = email_id[:13]
mail_right = email_id[13:]
mail_left = mail_left.split('_')
mail_right = mail_right.split('.')
print(mail_left[0])
print(mail_left[1])
print(mail_left[2])
print(mail_left[3])
print(mail_right[2])


#13b
print('Enter the single 5 digit number in list')
li = eval(input())
product = 1
for i in range(0,5):
    product = product*li[i]
print('Required product is : ',product)


#13a
print("Enter the date")
date = input()
ui= date.split('-')
print(ui[2:3])

#13
print('Enter the number')
x = int(input())
cfrac = x
for i in range(0,5):
    cfrac = x + 1/cfrac
print(round(cfrac,2))


# Q.no.12
print('Enter the string')
string = input()
start_index = int(input())
end_index = int(input()) + 1
sub_str = string[start_index : end_index]
new_str = ''
while(len(new_str)<len(string)):
    new_str = new_str + sub_str
print(new_str)




# Q.no 11
print('Enter the first number')
a = int(input())
print('Enter the second number')
b = int(input())
c = abs(a-b)
print("Difference of both the numbers are : ",c)
