import csv
def extract_lines(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    new = open("python.csv",'w')
    ff = csv.writer(new)
    for row in reader:
        if(row[2]== "M" and int(row[4]) >= 70):
            ff.writerow(row)
            print(row)
    new.close()
    f.close()
    read = open("python.csv",'r')
    readr = csv.reader(read)
    print(readr)
    for row in readr:
        print(row)
    read.close()
extract_lines("file.csv")