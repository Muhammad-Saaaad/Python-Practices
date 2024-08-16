# In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of 
# variables is crucial for writing efficient and maintainable code.

# Class Variable  : 
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any
#  method and are usually used to store information that is common to all instances of the class

class MyClass:
    Number=0  # Class variable 

    def __init__(self, name) -> None:
        self.name=name
    
    def par(self):
        MyClass.Number=10
        self.Number=1


obj1=MyClass('David')
obj2=MyClass('Jacks')
obj1.par()
print(obj1.Number) 
print(MyClass.Number)
# You can Acess the Class variuable my the name of the class or the by the instance(self).
# But when u Acess the variable from the Class name and change the Value of the Class variable by using the Class name , all the places where 
# the value of class variable is being used will be changed except for where the Class variable is being use by the instance name and we are
# changing the value by using the instance name 

# Instrance = Self keyword 

# Instance variable :

# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method 
# or inside any other method and are usually used to store information that is specific to each instance of the class.

class YourClass:
    def __init__(self , number) -> None:
        self.num=number  # instance variable 

obj1=YourClass(5)
obj2=YourClass(10)
obj3=YourClass(7)

print(obj1.num)
print(obj2.num)
print(obj3.num)

# Here as u can see that All three instance are using the same varible but due to the diference in the instance their value will be dependent 
# on the instance 