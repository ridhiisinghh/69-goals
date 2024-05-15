phone = input("Enter the 10 digit phone Number")
phn = list(phone)
print(phn)
for i in range(0,len(phn)):
    if(phn[i]=="o"):
        phn[i] = "0"
    if(phn[i]== "l"):
        phn[i] = "1"
if("o" in phone or "l" in phone):
    phone_no = ""
    for i in range(0,len(phn)):
        phone_no += phn[i]
    print(phone_no)
else:
    print("No mistake")
