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

# Class variables = Shared among all the instances of a class
#                   Defined outside the constructer
#                   Allow you to share data among all objects created from that class
class Student:
 
    class_year =2024 #Class variables
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1 #When you want to modify class variable it is a practice to access it with class name rather than self.(since its common to all class_instance)

student1 = Student("Rintaro",16)
student2 = Student("Kaoruko",15)
student3 = Student("Natsusawa",16)
print(student1.age)
print(student2.name)
print(student1.class_year)
print(Student.class_year)  # Access class variable with class name rather than its instance (since its common to all class_instance)
print(Student.num_students)
print(f'My graduating class of {Student.class_year} has {Student.num_students} students')


#Inheritance = Allows a class to inherit attributes & methods from other class
#              Helps with code reusability & extensibility

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):  #Childrens can have their own methods & attributes
    def speak(self):
        print("Bark!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Cow(Animal):
    def speak(self):
        print("Mooo!")


dog = Dog("Bruno")
cat = Cat("Garfield")
cow =Cow("Lady")

print(dog.name)
print(cat.is_alive)
dog.eat()
cow.sleep()
cow.speak()

# Multiple Inheritance = inherit from more than 1 parent class
#                        C(A,B)

# Multilevel Inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
# MULTIPLE 
class Prey:
    def flee(self):
        print("This animal is genius & fleed")

class Predator:
    def hunt(self):
        print("This animal is hunting for food")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator): #Inherit from more than 1 class
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

# MULTI-LEVEL
class Animal: # Grandparent class

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal): #Parent class
    def flee(self):
        print(f"{self.name} is genius & fleed")

class Predator(Animal): #Parent class
    def hunt(self):
        print(f"{self.name} is hunting for food")

class Rabbit(Prey): # Child class
    pass

class Hawk(Predator): # Child class
    pass

class Fish(Prey,Predator): #Inherit from more than 1 class # Child class
    pass

rabbit = Rabbit("Jimmy")
hawk = Hawk("Abel")
fish = Fish("Dory")

rabbit.eat()
hawk.sleep()
fish.eat()
fish.hunt()
