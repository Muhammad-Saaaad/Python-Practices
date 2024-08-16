# When a class is inherit from  another class the child class will have all the public and  protected methods and variables of parent class 
class Human:
    def __init__(self , gender , name):
        self.gender=gender
        self.name=name
    
    def show_details(self):
        print(f'{self.name} is a {self.gender} ')

obj=Human('Male', 'Harry')
obj.show_details()
#  Now to do inheritance 

class new_specie_1(Human): # Inheritance 
    # if u do not want to make the constructor then child class will automatically inherit the constructor of parent class called 
    # constructor inheritance but if u want to  add some extra in the constructor then u can make the constructor 
    def __init__(self, gender, name , feature): 
        super().__init__(gender, name)
        self.feature =feature

    # getter : 
    def getter_feature(self):
        return self.feature
    #setter
    def setter_feature(self , f):
        self.feature =f

s1=new_specie_1('Male','Zor','4 Arms')
s1.show_details()
print(s1.getter_feature())

class new_specie_2(Human):
    pass 

s2=new_specie_2('Female', 'Sara') 
s2.show_details()