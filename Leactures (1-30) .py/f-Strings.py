# F-Strings are use to add variables into the Strings 
 # Syntax 

  # simply write the keyword f before the String to make the String f String 
name = 'saad'
city='Islamabad'
fstr=f'hello my name is {name} and i am from {city}'
str='hi my name is ',name,'i am from ',city # don't write this it will consider it as tuple # noqa: E501
print(type(str),str)
print(fstr)
# or we can drictely write it as : 
print(f'hello my name is {name} and i am from {city}')
# if we want to Print the that where we put the varibale 
print(f'hello my name is {{name}} and i am from {{city}}')  # hello my name is {name} and i am from {city}  # noqa: E501, F541
 # so my putting {{}} double Curly bracses we can perfrom the previous Step

  # we can also perfrom this my .format() method but f-Strings are more convinient :
print('hello my name is {} and i am from {}'.format(name , city))  
# or we can also do this : 
print('hello my name is {1} and i am from {0}'.format(city,name)) 
# but f_String method is more pricise 

# Doc-Strings
 # Doc-Strings are those Strings that are wrriten at the very start of any funcation , method or class   # noqa: E501
 # Docstrings are used to associate the documentation with the objects like classes, methods and functions in python and   # noqa: E501
 #  they describe what the object does.  

def sum(a,b):
    ''' this funcation simply takes 2 numbers and give it sum as return'''  # Doc-String
    sum=a+b
    return sum
# we can acess the doc-String by using this funcation : 
print(sum.__doc__)  # output : this funcation simply takes 2 numbers and give it sum as return  # noqa: E501

# pep-8
 # its just a poem that is show when we write import this 