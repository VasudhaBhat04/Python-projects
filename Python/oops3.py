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
print(Employee.is_valid_position(""))
print(emp1.get_info())