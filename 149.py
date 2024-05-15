class StringManipulation:
    def __init__(self,L) -> None:
        self.words = L
    def total_words(self):
        self.n = len(self.words)
    def count(self,some_word):
        c=0
        for i in self.words:
            if(i==some_word):
                c+=1
        return c
    def words_of_length(self,length):
        c = []
        for i in range(0,len(self.words)):
            if(self.words[i]==length):
                c.append(self.words[i])
        return c
    def words_start_with(self,char):
        c = []
        for i in range(0,len(self.words)):
            if(self.words[i][0]==char):
                c.append(self.words[i])
        return c
    def longest_word(self):
        max = 0
        self.word = ""
        for i in range(0,len(self.words)):
            if(len(self.words[i]>max)):
                self.word = self.words[i]
        return self.word 
    def palindrome(self):
        self.li = []
        for i in range(0,len(self.words)):
            n = len(self.words[i])
            for j in range(0,n//2):
                if(self.words[i][j]==self.words[i][n-j]):
                    self.li.append(self.words[i])
        return self.li

S = StringManipulation(["ridhi","adda","adya","subbus","subbu"])
print(S.words_start_with("s"))
print(S.palindrome())

    
