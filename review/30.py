print("Enter the name of the person")
name1 = input()
print("Enter the date of birth")
dob1 = input()
print("Enter the name of the second person")
name2 = input()
print("Enter the date of birth")
dob2 = input()

if(dob1[-1:-5]<dob2[-1:-5]):
    print( name1 + " is younger")
    if(dob1[-1:-5]== dob2[-1:-5] and dob1[3:5]<dob2[3:5] ):
        print( name1 + " is younger")
        if(dob1[-1:-5]== dob2[-1:-5] and dob1[-5:-7]==dob2[-5:-7] and dob1[0:2]<dob2[0:2] ):
            print(name1 + " is younger")
        else:
            print(name2 + " is younger")
    else:
        print(name2 + " is younger")

else:
    print(name2 + " is younger")

