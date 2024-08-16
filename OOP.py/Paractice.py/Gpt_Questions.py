#1. Create a class called "Rectangle" with attributes "length" and "width" and methods to calculate its area and perimeter.
class Rectangle:

    length =0
    width = 0

    @classmethod
    def area(cls , length , width):
        cls.length =length
        cls.width = width 
        return cls.length * cls.width 
    
    @classmethod
    def parameter(cls , length , width):
        cls.length =length
        cls.width = width 
        return 2 *  (cls.length + cls.width)
    
obj=Rectangle()
print('Area of Rectangle : ',Rectangle.area(3 , 4))
print('Parameter of Rectangle', Rectangle.parameter(5,7))

#2. Implement a class hierarchy for different shapes, including a base class "Shape" and subclasses for "Circle," "Triangle," and "Rectangle."
#   Each subclass should have appropriate methods to calculate area and perimeter.

class Shape:# A hierachy means that a single parent can have multiple child classes 

    def area(self):
        pass 

    def parameter(self):
        pass

class Circle(Shape):

    def __init__(self , r) -> None:
        self.radius=r

    def area(self):
        return 3.1416 * self.radius*self.radius
    
    def parameter(self):
        return 2 * 3.1416 * self.radius
    
class Tringle(Shape):
    def __init__(self, base , height , length ):
        self.base=base
        self.height=height
        self.Length=length


    def area(self):
        return 0.5 * ( self.base * self.height)
    
    def parameter(self):
        return 3 * self.Length
    
class Rectangle(Shape):

    def __init__(self, length ,  width):
        self.width=width
        self.Length=length

    def area(self):
        return self.length * self.width 
    
    def parameter(self):
        return 2 *  (self.length + self.width)

options=0
obj_circle=Circle(5)
obj_rectangle=Rectangle(10 , 5 , 5)
obj_tringle=Tringle(5,3)
while options!=7:

    try:

        options=int(input('''Enter 1 for Area of Circle \nEnter 2 for Parameter of Circle 
Enter 3 for Area of Tringle \nEnter 4 for Parameter of Tringle 
Enter 5 for Area of Rectangle \nEnter 6 for Parameter of Rectangle \nEnter 7 to Exit : '''))
        
        match options:
            case 1 :
                print('Area of Circle : ', obj_circle.area())
            case 2 :
                print('Parameter of Circle : ', obj_circle.parameter())
            case 3 :
                print('Area of Tringle : ', obj_tringle.area())
            case 4 :
                print('parameter of Tringle (Equal sides ): ', obj_tringle.parameter())
            case 5 : 
                print('Area of Rectangle : ', obj_rectangle.area())
            case 6 :
                print('parameter of Rectangle : ', obj_rectangle.parameter())
            case 7 :
                print('Exit : ')
            case _:
                print('Invalid input : ')
    
    except ValueError:
        print('Inavlid input : ')
           

#3. Write a program that demonstrates the concept of method overriding by creating a base class "Animal" with a method "make_sound." 
#   Then, create subclasses "Dog" and "Cat," overriding the "make_sound" method to make appropriate sounds.

class Animal:
    def make_sound(self):
        print('Sound')

class Dog(Animal):
    def make_sound(self):
        # print('Waff Waff !!..') # you can also do this 
        return 'Waff Waff !!..'

class Cat(Animal):
    def make_sound(self):
        # print('Meow meow !!...')
        return 'Meow meow !!...'

dog_obj=Dog()
cat_obj=Cat()
print('cat sound',cat_obj.make_sound())
print('cat sound',dog_obj.make_sound())

#4. Create a class called "BankAccount" with attributes "account_number" and "balance." Implement methods to deposit and withdraw money, 
#   ensuring the balance doesn't go below zero.

class Bank:
    def __init__(self , acc) -> None:
        self.acc_number=acc
        self.balance=0

    def deposit(self):
        money=float(input('Enter money to deposit : '))
        if money <= 0:
            print( 'Invalid input ')
        else :
            self.balance=self.balance+money
            print('Transation Sucessfull : ')

    def withdraw_money(self):
        amount=float(input('Enter the amount you want to with draw from your account  : '))
        if amount <= 0:
            print( 'Invalid input ')
        elif amount > self.balance:
            print( 'Not Enough Balance : ')
        else :
            self.balance=self.balance-amount
            print('Transation Sucessfull : ')
           
# class ended 
options=0

acc_number=int(input('Enter your account number : '))
obj_bank=Bank(acc_number)

while options !=3:
    options=int(input('Enter 1 to Deposit : \nEnter 2 to With draw money : \nEnter 3 to Exit :'))
    
    match options:
        case 1:
            obj_bank.deposit()
        case 2 :
           obj_bank.withdraw_money()

#5. Implement the "Observer Pattern" by creating a class "Subject" that maintains a list of registered observers and notifies them 
#   when a change occurs. Create a class "Observer" that listens for updates from the subject.

class Observer:
    def update(self , data=None):
        if data == None:
            print('no Chnages occurres : ')
        else :
            print('Changes are : ' ,  data)

class Subject:
    def __init__(self) -> None:
        self. observer_list=[]

    def add_observer(self , observer):
        self.observer_list.append(observer)
        return 'oberver added'
    
    def remove_observer(self , observer):
        self.observer_list.remove(observer)
        return 'observer removed'

    def notifies_observer(self , data):
        for observer in self.observer_list:
            observer . update(data)

# Making 2 observer list : 
observer1=Observer() 
observer2=Observer()
observer3=Observer()

# Making a subject : 
sub=Subject()

# adding observers : 
print(sub.add_observer(observer1) , sub.add_observer(observer2) , sub.add_observer(observer3))

#notifing observer: 
sub.notifies_observer('Attention , your being  notified : ')

# removing observere : 
print(sub.remove_observer(observer2))

#notifing observer again : 
sub.notifies_observer('Attention , your being  notified again : ')



#6. Design a class "Student" with attributes "name," "age," and "marks" (a list of integers). Implement methods to calculate the
#   average and highest marks of a student.

class Student :
    def __init__(self , name , age , mark ) -> None:
        self.name=name
        self.age=age
        self.marks=mark

    def average(self):
        add=0
        for marks in self.marks : 
            add=add+marks
        
        return add/len(self.marks)
    
    def highest(self):
        highest=self.marks[0]
        for mark in self.marks:
            if mark > highest:
                highest=mark
        
        return  highest
    
student1=Student('David' , 18 , [50,78,99,87,70])
student2=Student('Jacks' , 20 , [90,87,98,80,70])

print(f"average of {student1.name}'s marks ", student1.average())
print(f"Highest marks  of {student1.name} is  : " , student1.highest())
print(f"average of {student2.name}'s marks ", student2.average())
print(f"Highest marks  of {student2.name} is  : " , student2.highest())

#7. Create an interface called "Shape" with methods "area" and "perimeter." Implement classes "Circle," "Triangle," and "Rectangle"
#   that implement the "Shape" interface.

from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass

class Circle(Shape):

    def __init__(self , r):
        self.radius=r

    def area(self):
        return 3.1416 * self.radius*self.radius
    
    def parameter(self):
        return 2 * 3.1416 * self.radius
    
class Tringle(Shape):
    def __init__(self, base , height , length ):
        self.base=base
        self.height=height
        self.Length=length


    def area(self):
        return 0.5 * ( self.base * self.height)
    
    def parameter(self):
        return 3 * self.Length
    
class Rectangle(Shape):

    def __init__(self, length ,  width):
        self.width=width
        self.Length=length

    def area(self):
        return self.Length * self.width 
    
    def parameter(self):
        return 2 *  (self.Length + self.width)
    
obj_circle=Circle(5)
obj_rectangle=Rectangle(10 , 5)
obj_tringle=Tringle(5,3 , 5)

print('Area of Circle : ', obj_circle.area())
print('Parameter of Circle : ', obj_circle.parameter())
print('Area of Tringle : ', obj_tringle.area())
print('parameter of Tringle (Equal sides ): ', obj_tringle.parameter())
print('Area of Rectangle : ', obj_rectangle.area())
print('parameter of Rectangle : ', obj_rectangle.parameter())

#9. Design a class "Person" with attributes "name" and "age." Implement the "Comparable" interface to allow sorting a list of persons 
#   based on their age.

class Compareable(ABC):

    @abstractmethod
    def sorting_age(self):
        pass

class Person(Compareable):
    __list=[]
    def __init__(self ,  name , age ):
        self.name=name
        self.age=age
        Person.__list.append(self.name)
        Person.__list.append(self.age)
        
    @classmethod
    def sorting_age(cls):
        age_list=Person.__list[1::2]

        new_list=sorted(age_list)
        return_list=[]
        for s in new_list:
            for name , b in zip( Person.__list[::2], Person.__list[1::2] ):
                if s == b:
                    return_list.append(name)
                    return_list.append(b)   
        
        return return_list

            
a=Person('Person1' , 13)
b=Person('Person2' , 12)
c=Person('Person3' , 15)
d=Person('Person4' , 10)

print(Person.sorting_age())
