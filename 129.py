class Word:
    word = input("ENTER ANY WORD")
    speech = input("Enter the speech")
    def print_info(self):
        print(self.word)
        print(self.speech)

p1 = Word()
p1.print_info()