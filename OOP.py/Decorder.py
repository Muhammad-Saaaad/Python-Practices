# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods.
# They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of 
# the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

# @decorator_function
# def my_function():
#     pass

# 1st u will Make a function that takes another function as an argument : 
def decorator_function(f): # This top function only take the function as an argument 
# 2nd add a new function inside the decorator function 
    def new_fun(): # and this only take or can't take (choice) the parameters as *args and **kwargs
        print('Hello : ')
        f()
        print('Thanks for using this function : ')
# 3rd after your done with the new function return the new function : 
    return new_fun

# 4th add the '@' sign with the name of decorator function and after that write the function which u want to passed in the new function of 
# decorator function
@decorator_function
def name():
    print('Saad')

# 5th siimply calls the name function : 
name()

# If the function asks for some arguments then : 
def decorator(fun):
    def inner_fun(*args , **kwargs):
        print('welcome sir')
        fun(*args , **kwargs)  # here if the number of values are simple they are taken as tuple and if they are in the from of key value 
        # then they are taken as dictionary 
        print('Thank you for using this function : ')
    return inner_fun
@decorator
def table(a):
    for i in range(1,11):
        print(a ,' * ',i,' = ',a*i)

table(4)
# or you can also do this  :
# after the 3rd Step : 

# 4th  step
def name2():
    print('saad')

# 5h step
decorator_function(name2)() # so simply we can also do this...


import logging

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

my_function(2,3)