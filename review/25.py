word = input()
count = {'a':0,'e':0,'i':0,'o':0,'u':0}
if('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
    if(word.index('a')<word.index('e')<word.index('i')<word.index('o')<word.index('u')):
        for char in range(0,len(word)):
            if(char in count.keys()):
                count[char] += 1
        if(count['a']>=count['e']>=count['i']>=count['o']>=count['u']):
            print("A perfect word")
else:
    print("not a perfect word")
           
