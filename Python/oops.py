# OOPS in python
#object = A "bundle" of related attributes(variables) and methods(functions)
#         You need a "class " to create many objects
#class = (blueprint) used to design the structure & layout of an object

class Car: #You can place  this is in a new file  [from car import Car]
    def __init__(self, model, year,color,for_sale): #constructer method 
        self.model = model                  #when we get the model name assign it to Car
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model} car")
    def stop(self):
        print(f'You stop the {self.model} car right now!!!')


car1 = Car("BMW", 2025, "Purple", False) 
car2 = Car("Corvette", 2024,"Red", True)   #Creating objects
print(car1.model)                               #attribute access operator
print(car1.year)
print(car2.for_sale)
car1.stop()
car2.drive()
