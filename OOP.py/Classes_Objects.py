# A class is a blueprint that have attributes and methods and define there structure and behaviuour with the class .

# Creating a  class : 
class person: # simply use class keyword and the name of the class 
    name='no name'
    gender='default'
    age=0
    def info(self): # In c++ , java  we use this keyword instead of self# But in python ,  to use sef we input self as the first parameter in the function 
        print(f'{self.name} is a {self.gender} having age {self.age} ')

# to make object from a class in java we use like this class obj=new class() 
# but in python we do this :

obj=person() # like in java we 1st write the name of class then object's name then new keyword and then the constructor 
# but in python we only write the object name with the constructor to make a object 

# know if we want to assign values we do this : 
person.info(obj) # You can see here that we have passed thge object as an Argument 
obj.name='saad'  #  this is how we can change the values 
obj.gender='boy'
obj.age=18
obj.info() # output : saad is a boy having age 18 
