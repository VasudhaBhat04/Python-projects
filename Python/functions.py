def func(): #function declaration
    print("Yohooo!")

func() # function call

#With parameters
def add(x,y):
    print(x+y)
add(3,2)

#Types of Arguments
#1.Positional arguments Values are matched to parameters by order
def intro(name, age):
    print(f"My name is {name} and I am {age} years old")

intro("Pani", 20)   # name="Alice", age=20
#intro(20, "Alice")   Wrong meaning: name=20, age="Alice"

#2. Keyword Arguments You specify the parameter name explicitly.Order doesn't matter.
def inc(name, age):
    print(f"My name is {name} and I am {age} years old")

inc(age=41, name="smi")

#3.Default Arguments You give parameters a default value.If the caller doesn’t provide a value, default is used.
def pizza(name, flavour="cheese"):
    print(f"I ate {name} pizza {flavour} flavoured")

pizza( name="dominozz") #no value for flavour param hence default will be used
pizza("dominozz","margerita") #margerita will be used

#4.Variable length Arguments Sometimes you don’t know how many inputs a user will pass.
#Python has two special types for this: *->unpacking operator
#can change the name but widely used kwargs or args after unpacking operator
# *args → Variable number of positional arguments.Collects extra arguments into a tuple.
def add_all(*args):
    print(args) 
    print(type(args))         # args is a tuple
    return sum(args)

print(add_all(1, 2, 3))          # 6
print(add_all(10, 20, 30, 40))   # 100

#**kwargs → Variable number of keyword arguments. Collects extra keyword arguments into a dictionary.
def show_details(**kwargs):
    print(kwargs)

show_details(name="Alice", age=20, city="Bangalore")
# {'name': 'Alice', 'age': 20, 'city': 'Bangalore'}

def addressof(**addr): 
    print(addr)
    print(type(addr)) #its a dictionary
 # already treat as dictionary
    for u in addr.values(): 
        print(u)            #prints inly values
    for v in addr.keys():
        print(v)            #prints only keys
addressof(street="102H",city="pae",state="zk",zip="123")
