# Python learning by myself
# This is comment

x=10 #Variable declaration
print(x)

z=str(10)#Type casting
print(z)
print(float(x))

print(type(x)) #type(variable) to get the datatype

a, b = "Mango", 'Papaya' #Strings in python, no char datatype in Python
print(type(a)) 
print(a)
print(len(b)) #len(string_varaible_name)
print(a[3]) # get the particular character from string 
print(10>9) #Boolean true

#Lists []
#allows duplicates , can modify the list, ordered, indexed
list =["apples","bananas","oranges"]
nom=[1,2,3,4]
print(list)
print(nom)
print(len(list))
print(list[2]) #indexed
list[2]="watermelon" #can modify
print(list)

#Sets {}
#no duplicates allowed, unordered , unidexed, since unindexed can't modify
set={"apples","bananas","oranges"}
som={1,2,3,4,1} #prints only {1, 2, 3, 4}
print(set)
print(som)
print(len(set))


#tuples ()
#allows duplicates, can't change, ordered, indexed
tuple =("apples","bananas","oranges","papayas", "cherry","bananas")
print(tuple)

#dictionaries {}
#key:value pairs , no duplicates ,ordered,can add new pair
dict={1:"bunny",2:'rabbit',3:"hare"}
print(dict)
print(len(dict))
print(dict[1]) #can access value through key-only

#for loops 
n=[1,2,3,4,5]
for x in n:
    print(x)
else:
    print("Exit the loop")

#if statements
a = 12
b = 124
if b > a:
  print("b is greater than a")
elif b < a: #else if is elif in python
   print("a is greater than b")
else:
   print("a & b are equal")

#While-loop, break & continue statements
i = 1
while i < 10:
  print(i)
  if i == 3:
     i += 1
     continue

  elif i == 7:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3: 
    continue #3 is skipped
  print(i)


# User input , input()
name=input('What is your name?')
print(f"Hello {name}") #f string is needed when you need to print the variables in a sentence
print(name) # no need of f string
xa = input() #user input
print(xa)
 
 #Pthon doesn't have array use lists[] instead
