import csv
def get_matrix(filename):
    f = open(filename,'r')
    reader = csv.reader(f)
    Matrix = []
    for row in reader:
        Matrix.append(row)
    print(Matrix)
get_matrix("file.csv")