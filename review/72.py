def check_leap_year(year):
    if(year%100==0):
        if(year%400==0):
            print("true")
    else:
         if(year%4==0):
             print("true")
         else:
            print("false")

check_leap_year(1604)
