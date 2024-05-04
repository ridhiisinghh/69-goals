def group_by_city(scores_dataset):
    cities = {}
    c = []
    for i in range(0,len(scores_dataset)):
        c.append(scores_dataset[i].get("city"))
    for i in c:
        list1 = []
        for j in range(0,len(scores_dataset)):
            if(scores_dataset[j].get("city")== i):
                list1.append(scores_dataset[j].get("name"))
            cities[i] = list1
    print(cities)

group_by_city([{"name": "Ridhi" , "city" : "ambikapur" },{"name" : "adya" , "city" : "banaras"},{"name" : "satyam" , "city" : "banaras"},{"name" : "aman" , "city" : "banaras"}])
