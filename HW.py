class Circle():
    def __init__ (self,r):
        self.radius = r
    
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*3.14*self.radius
    
radius = int(input('enter the radius off the circle'))
NewCirlce = Circle(radius)
print(NewCirlce.area())
print(NewCirlce.perimeter())