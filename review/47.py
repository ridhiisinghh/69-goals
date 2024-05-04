mark = int(input("Enter the marks for the question"))
option = int(input("Enter the number of option"))
correct = eval(input("Enter the sequence of correct option"))
ans = eval(input("Enter the sequence of option given by answer"))
num_of_ans = 0
for i in range(0,len(correct)):
    if(correct[i] == ans[i]):
        num_of_ans += 1
    else:
        num_of_ans = 0
print(num_of_ans)
n = option/len(correct)
marks_obtained = num_of_ans*n
print(marks_obtained)
