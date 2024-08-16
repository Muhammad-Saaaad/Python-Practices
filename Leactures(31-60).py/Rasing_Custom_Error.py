# In Exception Handling , if an error occures then we will Handle that error using exception Handling 
# but if suppose we want to make an error so that we can infrom the user that the value you have enterd is Wrong then we can rise custom error 

# KeyWord:raise

# Example : 
num=int(input('Enter a number between 1 to 5 : '))
if num<=1 or num >=5:
    raise ValueError('value out of range : ')
else :
    print('keep running the program')

# you can also make your own custom error by this : 
# In python , we can built a custom exception by making a new class and that is drived from the built - in exception class 
class myerror(Exception):
    pass # now u have your own custom error 

a=input('Enter any value for custom error : ')
try:
    raise myerror('Why you enter that value . ') # no you can use your own error but the progrm stops here 
except: # if you want to move use try except 
    print('move on : ')

# Practice Rising custom Error 

# Question 1 : Write a Python program that asks the user to input their age. Implement custom error handling to raise a ValueError if 
# the age entered is negative.

age=int(input('Enter your age : '))
if age <0:
    raise ValueError('Inavlid age ')   # Here you always neend to add an instance of the error class.

# Question 2 : Create a custom error class called InvalidEmailError. Write a function that takes an email address as input and 
# raises the InvalidEmailError if the email address does not contain the "@" symbol.

class InvalidEmailError(Exception):
    pass #  pass is use aholders a place, pass is use when a statment is required but no action is needed

email=input('Enter your email : ')
if '@' not in email:
    raise InvalidEmailError(' @ is missing in your email  : ') #output : InvalidEmailError:  @ is missing in your email :
else :
    print('keep going')

# Question 3 : Write a Python program that calculates the factorial of a positive integer entered by the user.
# Implement custom error handling to raise a ValueError if a non-positive integer is entered.

val=int(input('Enter a value to calculate its factorial : '))
if val <0:
    raise ValueError('Vlaue must be positive : ')
else :
    fac=1
    for i in range(1,val+1):
        fac=fac*i
    print('factoiral of ',val,' is ',fac)


# Quick Quiz : 
# write a program that get the integer value between 1 to 5 if user enters quit it will not show error other wise show error

value=input('Enter a value : ')
if value != 'quit' and (value <='1' or value >='5'):
    raise ValueError
else:
    print('no error : ')