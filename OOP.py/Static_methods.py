#In Python, you can create a static method using the @staticmethod decorator. A static method is a method that belongs to a class rather 
# than an instance of the class. It does not have access to the instance (self) or the class (cls) itself. Static methods are defined using 
# the @staticmethod decorator, and they do not require the self or cls parameters as the first argument.

class MyClass:
    def __init__(self) -> None:
        self.x=90
    def non_static_method(self):
        print('This is a non static method ' , self.x)

    @staticmethod
    def static_method(a,b):   # No self keyword # No acess to the  outside  methods or attributes 
        print('This is a static method : ',a+b)

obj1=MyClass()
obj1.non_static_method()   # Non _static methods cannot be called by the Class name 
obj1.static_method(2,5)
MyClass.static_method(9,8)   # They can be called by using obj and also the class name 