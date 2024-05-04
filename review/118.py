import csv
filename = "file.csv"
def get_dict(filename):
    f = open(filename,"r")
    L = f.readlines()
    keys = []
    values = []
    for x in L:
        short = x.split(",")
        keys.append(short[0])
        values.append(short[1][:-1])
    print(keys)
    print(values)
    dict = {}
    for i in range(1,len(keys)):
        dict[keys[i]] = values[i]
    print(dict)

get_dict(filename)