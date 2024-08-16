# Import function is use to import code Script from the imported module into your current Script and also import that code that is associted 
# with the imported Script 
# This allows you to use all those function , methods and classes in that Script 

# One important this u need to understand is , when u import a module all the code in the module will firstly executed and then u can 
# all the function , methods and classes in the module

import math # now your able to use all the function , methods and classes in the math module 

print(math.sqrt(9))

# if u only want to import a specfic functions use can use From keyword 

from math import sqrt , pi # after this u don't need to add math. with these functions 

print(sqrt(9)*pi)


print(sqrt.__doc__) # to check what the function does 


# You can also import all the functions using the * keyword 
# from math import * # but this is not a good apporach as it confused the compiler that which function is from from which module 

# Python also allows you to rename imported modules using the 'as' keyword. This can be useful if you want to use a shorter or more
# descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.

import math as m 
print(m.factorial(5))
print(m.sqrt(49)*m.pi)

# you can also use a dir function that is a built in function use to print all the varibale and functions use in the specfic module 

print('abc',dir(m))

if 'sqrt' in dir(m): # to find if the specfic thing exist or not in the module 
    print('yes')

import if__name____main__ as imp_mod

imp_mod.fun()   # output: code inside the function : 
print(imp_mod.__name__)  # output:  if__name____main__ 