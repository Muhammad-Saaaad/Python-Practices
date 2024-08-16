# The 1st pillier of OOP  is  Called Encaplusition (Data hiding)
#   That can be achieved by using Getters and Setters 

# making my own getter and setter

class circle:
    def __init__(self) -> None:
        self.radius=0
    
    def getter_radius(self):
        return self.radius
    
    def setter_radius(self , radius):
        self.radius=radius

obj=circle()
print(obj.getter_radius()) 
print(obj.setter_radius(9))
print(obj.getter_radius())
print(obj.getter_radius)

