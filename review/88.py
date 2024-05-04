n = int(input("Enter the number of students"))
list1 = []
for i in range(0,n):
    dict1 = {}
    dict1["Name"] = input("Enter the Name")
    dict1["City"] = input("Enter the city")
    dict1["SeqNo"] = int(input("Enter the seqno"))
    dict1["Mathematics"] = int(input("Enter the Marks"))
    dict1["Physics"] = int(input("Enter the Marks"))
    dict1["Chemistry"] = int(input("Enter the Marks"))
    list1.append(dict1)
print(list1)
