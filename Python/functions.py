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

def hello(*args, **kwargs):
    for arg in args: #if you dont want it to dispaly as a list but indivial no.s
        print(arg, end=" ") #end="" prints in single line
    print()
    print(kwargs)

hello(1,23,4,2,6,color="pink",flower="lotus")

#Iterables An object or collection  taht acn return its elements one at a time,allowing it to be iterated over a loop.
#tuples, lists, sets, string, dict
#list iterable
x=[1,2,3,4,5]
for n in x:
    print(n,end=" - ")
print()
    
for i in reversed(x): #reversed() 
    print(i,end="-")
print()

#tuples iterable
xp=(1,2,3,4,5)
for ip in reversed(xp): #reversed() 
    print(ip,end=" ")
print()

#set iterable
set={"Hello","Good","Morning"}
for word in set: # U can't reverse a set 
    print(word,end=" <3 ")
print()

#String iterable
str="Stranger Things"
for c in str:
    print(c,end="*")

print()
#Dictionary iterable
dict= {"a":"avacado","b":"bhindi","c":"cherry_tomatoes"}
for key in dict.keys():
    print(key,end=" ")
print()
for val in dict.values():
    print(val,end=",")

#Memership operators :test whether value/ variable found in sequence
#in or  not in
#tuples, lists, sets, string, dict


string = "Classmate notebooks are awesome" #rem:case sensitive
x=input("Enter the word: ")

if x in string:
    print(f'{x} found')
elif x not in string:
     print(f'{x} not found')

# list compressions (for-each loop)a concise way to create lists in Python
#[expression for value in iteratble if condition]
doubles = []
for x in range(1,11):
    doubles.append(x*x)
print(doubles)

#or

doublesa =[x*x for x in range(1,11)]#[expression for value in iteratble if condition]
print(doublesa)

triples=[z*3 for z in range(1,11)]
print(triples)

numbe =[1, -2, -3, 4, -5]
pos=[num for num in numbe if num>=0]
neg=[num for num in numbe if num<0] #for every num in numbe check if the num is positive if so return the num
print(neg)
print(pos)






