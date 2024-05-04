def get_toppers(scores_dataset,subject,gender):
    toppers = []
    students = {}
    max = 0
    for i in range(0,len(scores_dataset)):
        if(scores_dataset[i].get(subject)>max):
            max = scores_dataset[i].get(subject)
    for i in range(0,len(scores_dataset)):
        if(scores_dataset[i].get("gender")== gender):
            students[scores_dataset[i].get("Name")] = scores_dataset[i].get(subject)
    for i in range(0,len(students)):
        if(students[i]== max):
            toppers.append(students[i])
    return toppers
