list1 = eval(input())
freq = {}
for word in list1:
    if(word in freq.keys()):
       freq[word] += 1
    else:
        freq[word] = 1
print(freq)
