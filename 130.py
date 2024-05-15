class point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def distance(self,x1,y1):
        self.distance = abs(x1-self.x)+abs(y1-self.y)
        return self.distance
    def is_origin(self):
        if(self.x==0 and self.y==0):
            return True
        else:
            return False
    def on_xaxis(self):
        if(self.x == 0):
            return True
        else:
            return False
    def on_yaxis(self):
        if(self.y==0):
            return True
        else:
            return False
    def quadrant(self):
        if(self.x>0 and self.y>0):
            return "First"
        elif(self.x>0 and self.y<0):
            return "Fourth"
        elif(self.x<0 and self.y>0):
            return "second"
        elif(self.x<0 and self.y<0):
            return "Third"
        else:
            return "On axis or origin"
    def slope(self):
        if(self.y!=0):
            self.slope = abs(0-self.x)/abs(0-self.y)
            return self.slope

P = point(12,30)
print(P.distance(10,15))
