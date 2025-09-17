# variable scope = where a variable is visible & accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():  # variables declared within a function have a local scope
    a=1       # a is local to the func1
    print(a)
    
def func2():  # functions cannot see what's there in another function
    b=2
    print(b)

func1()
func2()

def func3():
    c=2
    def func4():
        c=3      #Locals will be used first
        print(c) #if c wasn't declared in func4 then use enclosed c=2 & will print 2
    func4()
func3()

def func5():
    print(d)

def func6():   
        print(d)

d=3 #Global variables
func5()
func6()

from math import e

def func7():
    print(e)

e=4 #local version will be printed , if not e = 2.71 which is a built_in variable in math will be printed
func7()

        