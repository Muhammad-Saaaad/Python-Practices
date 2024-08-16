li=[1,2,3,4,5]
# Suppose u want to convert all the element of the list into there cubeic form 
#  1 . is you apply for loop and then import each value then perfrom the operation on each value and append it into a new list 
#  2 . you use a map  function ...(map() returns a object so it is important to type cast that object : )

# Map Syntax:
# map(function , iterateable)
def cube(n):
    return n*n*n
new_list=list(map(cube, li))
print('map ',new_list)
#  You can also use lambda functions : 
new_list=list(map(lambda x : x*x*x , li))
print('map with lambda ',new_list)

# Map define: 
#   The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
#   The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, 
#   or any other iterable object.




#  Suppose u want to find the numbers from the list that meets the condation of the function that returns True . 
# Use Filter() :
# Syntax :

# filer(function , iterateable)

def fun(x):
    # return True if x >3 else False
    return x>3

new_list=list(filter(fun, li)) # Filter also  returns a object so we neend to type cast it : 
print('filer ',new_list)
new_list=tuple(filter(lambda x :x>3 , li ))
print('filter with lambda ',type(new_list),new_list)

#   Filter define:
#   The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a
#   new sequence containing only the elements that meet the predicate.
#   The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. 
#   The iterable argument can be a list, tuple, or any other iterable object.



#  reduce()

# The reduce function is a higher-order function that applies a function to a sequence and returns a single value.
#  It is a part of the functools module in Python and has the following syntax:

# Syntax:
# reduce(function, iterable)

# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements,
#  such as a list or tuple.
# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the
#  next element, and so on. The reduce function returns the final result.

from functools import reduce

li=[23,43,1,23,12,32,90,2]

def max(x,y):
    return x  if x > y else y 

max_value=reduce(max ,  li)
print('reduce ',max_value)  # output : reduce  90

max_value=reduce(lambda x , y : x if x>y else y , li) # rembember there is no return statment in the lambda function 
print('reduce with lambda ',max_value)