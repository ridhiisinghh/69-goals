backlogs = int(input("ENTER THE NO OF BACKLOGS:"))
CGPA = float(input("ENTER YOUR CGPA"))
if(backlogs >5 or CGPA <6):
       print('Not Selected')
else: 
      print('Selected ')
      package = 5 * CGPA 
      print(package ,"lakhs")
