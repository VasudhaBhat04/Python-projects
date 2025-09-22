# Super class : Function used in a child class to call methods from a parent class(super class)
#               Allows you to extend the functionality of the inherited methods

class Shapes:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shapes):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

    def describe(self):     # Method overriding:if parent & child both shares same method name then child's method is considered
        print(f"Area is {self.radius*self.radius*3.14} cm.sq")
        super().describe()  # If u still need describe method of parent class

class Sqaure(Shapes):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled) #Super function to reuse the constructor of Parent class in Child class
        self.width=width

    def describe(self):     
        print(f"Area is {self.width*self.width} cm.sq")
        super().describe() 

class Trainge(Shapes):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height
    
    def describe(self):     
            print(f"Area is {self.width*self.height} cm.sq")
            super().describe() 

circ = Circle("Pink",True,5)
sq = Sqaure("Blue",False,7)
tri = Trainge("Yellow",True,6,7)

print(circ.color)
print(sq.is_filled)
print(tri.height)
circ.describe()
sq.describe()
tri.describe()