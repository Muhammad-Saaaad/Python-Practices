# A constructor is a special method in a class used to create and initialize an object of a class.
class myclass:
    # __init__ is the keyword to make a constructor : 
    def __init__(self , name , age):# When u make an object the object is automatically passed to the self keyword and its very important to
        #  use self with every method of the class , self also works as 'this' keyword 
        self.name=name # this  will give the value to the name when calling a constructor 
        self.age=age

    def information(self): # as the object is passed to the self the data in the object is know being use in this method 
        # print(f'{name}') if u write this it will give error at name 
        print(f'{self.name} is {self.age} years old')

obj1=myclass('Saad',18)
obj2=myclass('Harry',24)

obj1.information()
obj2.information()

# There are 3 types of constructors : 
# 1 :  Default constructor 
#  If u do not make a constructor in the class 
# 2 : Parametrize constructor
#  if u give some  parameters to the constructor along with the self keyword like the one above
# 3 : non-parametrize constructor 
#  if u do not give some  parameters to the constructor along with the self keyword is Called non-parametrize constructor
# Example : 

class no_parameter:
    def __init__(self):
        pass