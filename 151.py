class Time:
    def __init__(self,time) -> None:
        self.seconds = time
    def seconds_to_min(self):
        self.min = self.seconds//60
        self.seconds = self.seconds%60
        print(self.min,"min ",self.seconds,"secs ")
    def seconds_to_hours(self):
        self.hours = self.seconds//3600
        self.min = (self.seconds%3600)//60
        self.seconds = (self.seconds%3600)%60
        print(self.hours,"hours ", self.min,"min ",self.seconds,"secs ")
    def seconds_to_days(self):
        self.days = self.seconds//86400
        self.hours = (self.seconds%86400)//3600
        self.min = ((self.seconds%86400)%3600)//60
        self.seconds = ((self.seconds%86400)%3600)%60
        print(self.days,"days ",  self.hours,"hours ", self.min,"min ",self.seconds,"secs ")
T = Time(86460)
T.seconds_to_days()