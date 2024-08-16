# class Calculator:
#     __Hour=0
#     __Min=0
#     def menu(self):
#         option=0
#         while option !=9:
#             try:
#                 option=int(input('''
# Enter 1. Set Hour 
# Enter 2. Set Minute
# Enter 3. Get Hour 
# Enter 4. Get Minute
# Enter 5. Add Minutes 
# Enter 6. Substract Minutes
# Enter 7. Add Time
# Enter 8. Show Time 
#         '''))
#                 match option:
#                     case 1:
#                         hour=int(input('Enter Hour : '))
#                         self.set_hour(hour)
#                     case 2 :
#                         minutes=int(input('Enter minutes : '))
#                         self.set_Minutes(minutes)
#                     case 3:
#                         print('Hour : ',self.get_hour())
#                     case 4:
#                         print('Minutes : ',self.get_minutes())
#                     case 5:
#                         minutes=int(input('Enter minutes to b added :'))
#                         self.add_minutes(minutes)
#                     case 6:
#                         minutes=int(input('Enter minutes to b Substracted :'))
#                         self.substract_minutes(minutes)
#                     case 7:
#                         hour=int(input('Enter hour to b added : '))
#                         minutes=int(input('Enter minutes to b added : '))
#                         self.add_time(hour , minutes)
#                     case 8:
#                         self.show_Time()
#                     case 9:
#                         print('Exit : ')
#                     case _:
#                         print('Invalid input : ')
            
#             except ValueError:
#                 print('Invalid input :')

    
#     def set_hour(self , hour):
#         Calculator.__Hour=hour
    
#     def set_Minutes(self , minutes):
#         Calculator.__Min=minutes

#     def get_hour(self):
#         return Calculator.__Hour

#     def get_minutes(self):
#         return Calculator.__Min
    
#     def add_minutes(self , minutes):
#         if minutes > 60:
#             print('Cannot enter more than 60 :')
#             return False
#         else:
#             extra_min=0
#             if self.get_minutes() + minutes > 60:
#                 extra_min = (self.get_minutes() + minutes) - 60
#                 self.set_hour(self.get_hour() + 1)
#                 self.set_Minutes(extra_min)
#             else :
#                 self.set_Minutes(self.get_minutes() + minutes)
#             print('Minutes added sucessfully ')
    
#     def substract_minutes(self , minutes):
#         if minutes > 60:
#             print('Cannot enter more than 60 :')
#             return False
#         else :
#             extra_min=0
#             if self.get_minutes() - minutes < 0 :
#                 extra_min=(minutes-self.get_minutes())
#                 self.set_hour(self.get_hour() -1 )
#                 self.set_Minutes(60-extra_min)
#             else :
#                 self.set_Minutes(self.get_minutes() - minutes)
#             print('Time substracted sucessfully : ')

#     def add_time(self , hour , minutes):
#         if hour > 12 or minutes > 60 :
#             print('Enter a shorter time : ')
#             return False
#         else :
#             if self.get_hour() + hour >12:
#                 extra_hour=(self.get_hour() + hour) -12
#                 self.set_hour(extra_hour)
#             else :
#                 self.set_hour(self.get_hour() + hour)
#             print('Hour Added Sucessfully : ')
#             extra_min=0
#             if self.get_minutes() + minutes > 60:
#                 extra_min = (self.get_minutes() + minutes) - 60
#                 self.set_hour(self.get_hour() + 1)
#                 self.set_Minutes(extra_min)
#             else :
#                 self.set_Minutes(self.get_minutes() + minutes)
#             print('Minutes added sucessfully ')

#     def show_Time(self):
#         print(f'{self.get_hour()} : {self.get_minutes()}')

# obj1=Calculator()
# obj1.menu()


# Shape Hierarchy:
# Create a shape hierarchy using inheritance. Define a base class Shape with a method area() that returns the area of the shape as 0.
#  Then, create subclasses Rectangle and Circle. Override the area() method in each subclass to calculate and return the area of the 
#  corresponding shape.

# class Shape:
#     def area(self , r):
#         return 0
    
# class Circle(Shape):
#     def area(self , r):
#         return 3.1416*r*r
    
# class Rectangle(Shape):
#     def area(self , r):
#         return r*4
    
# obj1=Circle()
# obj2=Rectangle()
# print(obj1.area(5))
# print(obj2.area(5))

# Bank Account Inheritance:
# Create a BankAccount class with attributes account_number, account_holder, and balance. Include methods for deposit, withdrawal, and
# checking the balance. Then, create subclasses SavingsAccount and CheckingAccount. The SavingsAccount should have an additional attribute
# interest_rate and a method to calculate and add interest to the balance.

class BankAccount:
    def __init__(self , a_n , a_h  , balance) -> None:
        self.account_number =a_n
        self.account_holder = a_h
        self.balance=0

    def deposit(self):
        self.balance=float(input('Enter amount to b deposit into your account : '))
        print('Money deposit sucessfully : ')

    def withdrawal(self):
        balance=float(input('Enter your balance : '))
        if self.balance >= balance : 
            self.balance-balance
            print('Transation sucessfull : ')
    def check_balance(self):
        print('Your balance is : ' , self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, a_n, a_h, balance ) -> None:
        super().__init__(a_n, a_h, balance) # here there is a () with super also you need to call the constructor name also 
        self . limit_rate=50000

    def interest_rate_calculate(self):
        if self.balance > 50000 and self.balance < 1000000:
            self.limit_rate=(self.balance/0.2)+self.limit_rate
        elif self.balance > 100000 and self.balance < 200000 :
            self .limit_rate = (self.balance/0.5)+self.limit_rate
        elif self.balance > 200000 :
            self . limit_rate= (self.balance/0.7)+self.limit_rate

class CheckingAccount(BankAccount):
    pass



# Vehicle Inheritance:
# Create a Vehicle class with attributes make, model, and year. Then, create subclasses Car, Motorcycle, and Truck. Add additional
#  attributes and methods to each subclass that are specific to the vehicle type. For example, Car might have attributes like num_doors
#  and convertible, and methods like start() and stop().

class vehical:
    def __init__(self , make , model , year) -> None:
        self.make=make
        self.model=model
        self.year=year
    
class Car(vehical):
    def __init__(self , make , model , year , num_doors , convertible) -> None:
        super().__init__(make , model , year)
        self . doors=num_doors
        self . convertable=convertible

    def start(self):
        print('car is started : ')
    def stop (self):
        print('Car is Stoped : ')
    
class truck(vehical):
    def __init__(self , make , model , year , num_tyrs , type):
        super().__init__(make , model , year)
        self. tyrs=num_tyrs
        self. type = type

class bike(vehical):
    def __init__(self, make, model, year , engine , maximum_speed) -> None:
        super().__init__(make, model, year)
        self . engine = engine 
        self . maximum_speed = maximum_speed

obj_car=Car('Us' , 'Neon' , 2023 , 4 , True)
obj_truck=truck('Canada' , 'tesla' , 2022 , 8 , 'Electric')
obj_bike=bike('Japan' , 'Hayabuusa' ,  2020 , 'Cobra 3000' , '250  km/H')

obj_car.start()
obj_car.stop()

