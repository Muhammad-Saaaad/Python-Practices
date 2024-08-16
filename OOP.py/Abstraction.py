# In Python, you can create abstract methods and abstract classes using the abc (Abstract Base Classes) module. The abc module provides 
# the necessary tools to define abstract classes and methods, which are classes and methods that are meant to be overridden by subclasses.

# Here's how you can create an abstract method and an abstract class in Python using the abc module:

# Abstract Method:
# An abstract method is a method declared in an abstract class but does not have any implementation. Subclasses of the abstract class 
# must provide their own implementation for the abstract method.

# Abstract Class:
# An abstract class is a class that cannot be instantiated directly and contains one or more abstract methods. It serves as a blueprint 
# for other classes and must be subclassed to create objects.


from abc import ABC , abstractmethod

class Shape (ABC):   # Abstract class . also an interface 
    # Making a Abstract method : 
    @abstractmethod
    def area(self):
        pass

class circle(Shape):
    def __init__(self , r) -> None:
        self.radius = r

    def area(self):
        return self.radius*4
    
obj=circle(5)

print(obj.area())