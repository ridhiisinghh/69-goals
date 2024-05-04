def letter(let1,let2):
    dist = abs(let2 - let1) 
    return dist

def distance(word1,word2):
    if(len(word1)==len(word2)):
        total = 0
        for i in range(0,len(word1)):
            distance = letter(ord(word1[i]),ord(word2[i]))
            total += distance
        print(total)
    else:
        print(-1)
word1 = "dog"
word2 = "cat"
distance(word1,word2)
