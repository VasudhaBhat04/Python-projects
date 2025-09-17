# module = a file containing code you want to include in your program
# use 'import' to include a module (build-in or your own)
# useful to break up a large program reusable sepearte files.

print(help("modules")) # list of all module available in python

print(help("math")) #lists all the variables & functions in particular module

import math
print(math.pi)

#or 

import math as m # alias name 
print(m.pi)

#or
 
from math import pi #can have name conflicts
print(pi)

import example as ex

result = ex.pi
result = ex.square(2)
result = ex.cube(3)
result = ex.area(4)
result = ex.circumference(5)
print(round(result,2))