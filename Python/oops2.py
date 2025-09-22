# Super class : Function used in a child class to call methods from a parent class(super class)
#               Allows you to extend the functionality of the inherited methods

class Shapes:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shapes):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

class Sqaure(Shapes):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width

class Trainge(Shapes):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height

circ = Circle("Pink",True,5)
sq = Sqaure("Blue",False,7)
tri = Trainge("Yellow",True,6,7)

print(circ.color)
print(sq.is_filled)
print(tri.height)