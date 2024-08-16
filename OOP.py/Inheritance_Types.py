# Single Inheritance : 
# Inheritance having one Parent class and one child class 
class parent:
    pass
class child(parent):
    pass
# Muntiple Inheritance : 
# Inheritance with 1 Child Class but muntiple parent classes 
# If there are 2 methods of the same name then the parent that is called 1st will b printed not the parent that is on the 2nd or so on 

# first parent that was taken , his constructor can  b call again
# Also if there is a method that has the same name in both of the parent classes then for that the method in the 1st parent class will be called
class parent1:
    def __init__(self , attribute) : 
        self.attibute=attribute

    def show1(self):
        print("This is parent1's method")

class parent2:
    def __init__(self , variable) : 
        self.variable=variable
    def show2(self):
        print("This is parent2's method")

class child(parent1,parent2):
    def __init__(self, attribute):
        super().__init__(attribute)

obj=child(1)
obj.show1()   # output: This is parent1's method
obj.show2()   # output: This is parent2's method

#Multilevel Inheritance is that in which there is a Parent class that has a Child class and the child class also has another child class 
class parent1:
    pass 
class child1(parent1):
    pass
class child2(child1):
    pass

# Hybrid Inheritance : 
# Inheritance that is made up of single inheritance and muntiple inheritance 
class A:
    pass
class B(A): #  Single inheritance 
    pass
class C(A):
    pass
class D(B , C): # Muntiple Inheritance
    pass 

# Herarical Inheritance :
# Inheritnace that fallows a Hararchi .
# Suppose there is a parent and it has 2  childs and both of the  childs also have their own child as well 

class Z:
    pass
class Y(Z):
    pass 
class X(Z):
    pass
class L(X):
    pass
class M(Y):
    pass 
