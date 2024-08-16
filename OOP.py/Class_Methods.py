# In Python, classes are a way to define custom data types that can store data and define functions that can manipulate that data.
# One type of function that can be defined within a class is called a "method." 
class MyClass:
    num=0 # Class Variable  
    @classmethod # Use to make a class method 
    def mymethod(cls , number):
        cls.num=number

obj=MyClass()
obj.mymethod(10)
print(obj.num) # Know the value of  num is change peremntaly 

# Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific
#  instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that
#   operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and 
#   organized code in Python.