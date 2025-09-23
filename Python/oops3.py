# Static methos = A method that belong to class rather than any object from that class(instance)
#                 Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility function that do not need access to class data
class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod              # It belongs to class not any object created from that class
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","CEO","CFO"]
        return position in valid_positions
    
emp1 = Employee("Nala","CEO")
emp2 = Employee("Luna","Cashier") 
print(Employee.is_valid_position("")) #Static method you can access with the class
print(emp1.get_info()) # For instance method you need to create an object then access the method with object

# Class Methods = Allow operation related to class itself
#                 Take (cls) as the first parameter, which represents the class itself.

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):     #Instance method
        return print(f"{self.name} has {self.gpa} gpa")
    
    @classmethod
    def get_count(cls):
        return f"Total no. of students is {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls): #Cls as first parameter
        if cls.count == 0:
           return
        else:
            return f"{cls.total_gpa/cls.count:.2f}"
        
s1 = Student("Oggy",3.2)
s2 = Student("Jack",2.6)
s3 = Student("Olivia",3.8)
s1.get_info()
    
print(Student.get_count())
print(Student.get_avg_gpa())

# Magic methods / Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many of Python's built in operations
# They allow developers to define/ customize the behaviour of objects
 
class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):   #String representation of object
        return f"{self.title} by {self.author}"
     
    def __eq__(self,other): # Check 2 objects are equal
        return self.title == other.title and self.author == other.author
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == "title":
            return self.title
        
        if key == "author":
            return self.author
        
b1 = Book("Harry potter","J.K Rowling",1024)
b2 = Book("Dune:Prophecy","Frank Herbert",234)
b3 = Book("Harry potter","J.K Rowling",1024)
print(b1)
print(b2)
print(b1 == b3)
print(b1 < b2)
print(b3 > b2)
print(b1 + b2)
print("Prophecy" in b2)
print("Prophecy" in b1)
print("Rowling" in b3)
print(b1["title"])
print(b2["author"])
