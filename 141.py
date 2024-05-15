class Signal:
    def __init__(self,T) -> None:
        self.state = "red"
        self.threshold = T
        self.vehicle = 0
    def sense(self,vd):
        self.vehicle = vd
    def update(self):
        if(self.state == "red" and self.vehicle>=self.threshold):
            self.state == "Green"
            self.vehicle = 0
        if(self.state== "Green" and self.vehicle>=self.threshold):
            self.state == "red"
            self.vehicle = 0
    def show(self):
        return self.state
            
S = Signal(30)
S.sense(34)
S.update()
print(S.show())
S.sense(24)
S.update()
print(S.show())