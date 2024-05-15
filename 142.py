class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def print_info(self):
        print("(",self.x,",",self.y,")")
    def scale(self,s):
        self.x = s*self.x
        self.y = s*self.y
    def reflect_about_x(self):
        self.y = self.y - (2*self.y)
    def reflect_about_y(self):
        self.x = self.x - (2*self.x)
    def add(self,):


