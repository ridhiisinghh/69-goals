class Shape:
    def __init__(self,name) -> None:
        self.name = name

class Square(Shape):
    def __init__(self, name, side) -> None:
        super().__init__(name)
        self.side = side
        self.compute_area = side*side
        self.compute_perimeter = 4*side
    def compute_Area(self):
        return self.compute_area
    def compute_Perimeter(self):
        return self.compute_perimeter
    
S = Square("Square",4)
print(S.compute_Perimeter())
