scores_dataset = []
n = int(input("Number of element"))
for i in range(0,n):
    dict1 = { "SeqNo" : int(input("sequence")), "maths" : int(input("maths ka number")), "sci" : int(input("science ka number")), "sst" : int(input("sst ka number")), "Name" : input() , "Gender" : input() , "City" : input()}
    scores_dataset.append(dict1)
def get_marks(scores_dataset,subject):
    lst = []
    for j in range(0,len(scores_dataset)):
        for i in dict1:
            if(dict1[i]== subject):
                lst.append((dict1["Name"],dict1[i]))
            else:
                print("No such subject is there")
    print(lst)

get_marks(scores_dataset,maths)
