import csv
def get_goals(filename,country):
    f = open(filename,'r')
    reader = csv.reader(f)
    num_players = 0
    num_goals = 0
    for row in reader:
        if(row[1]== country):
            num_players += 1
            num_goals+=int(row[2])
            tup = (num_players,num_goals)
        else:
            tup = (-1,-1)
    print(tup)
    f.close()
    
get_goals("file.csv","Brazil")