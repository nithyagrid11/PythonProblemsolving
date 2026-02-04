'''class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x1-x2) ** 2 + (y1-y2) ** 2) * 0.05
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (4,5)
coords = Line(coordinate1,coordinate2)
print(coords.distance())
print(coords.slope())'''

class Cylinder:
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * ((self.radius)**2) * self.height
    
    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.radius + self.height)
c = Cylinder()
print(c.volume())
print(c.surface_area())
