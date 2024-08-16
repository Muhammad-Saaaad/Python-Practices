listing=[5,54,6548,484,54,6546,456,465,4,845,4,51,84,251,21,4,87,45,48,43544]
# we have to find the odd number  using lambda function and a filter : 

# odd_list=list(filter(lambda x : True if x%2!=0 else False , listing))
# odd_list=list(filter(lambda x : x if x%2!=0 else False , listing))
odd_list=list(filter(lambda x : x%2!=0  , listing))
print(odd_list)

# Question: Given a list of strings, sort the strings based on their lengths using the sorted() function and a lambda function as the key.

# sorted() syntax : 
# sorted_list = sorted(iterable, key=None, reverse=False)


words = ["apple", "banana", "orange", "grapes", "watermelon"]

list_sorting=sorted(words , key=lambda x : len(x))
print('sorting use list : ',list_sorting)

# Question: Create a list of the squares of the first 10 positive integers using the map() function and a lambda function.

num=range(1,11)  # simple range contain number that cannot drictely use with any operation but can b used with the functions and can b use 
# as a iterateable 
square=list(map(lambda x : x*2 , num))
print(square, type(square))


# Question: Given a list of names, create a new list containing only the names that start with the letter 'A' using a lambda function and 
# the filter() function.

names = ["Alice", "Bob", "Alex", "Charlie", "Amy"]

A_names=list(filter(lambda x : x.startswith('A') , names))

print(A_names)

# Question: Use a lambda function to compute the product of all elements in a list.
from functools import reduce
num=range(1,6)
product=reduce(lambda x,y : x*y , num)

print(product)