# # class Employee:

# #     def  calculate_bonus (fun):
# #         def inner_fun(self,*args): # if the function is constructor then pass the self keryword otherwise don't pass it 
# #             fun(self,*args)
# #             if self.salary <=50000:
# #                 print(f'{self.name} has salary about {self.salary} also having bonus {self.salary*0.1} ')
# #             elif self.salary > 50000 and self.salary < 100000:
# #                 print(f'{self.name} has salary about {self.salary} also having bonus {self.salary*0.15} ')
# #             elif self.salary > 100000 :
# #                 print(f'{self.name} has salary about {self.salary} also having bonus {self.salary*0.2} ')
# #         return inner_fun

# #     @calculate_bonus
# #     def __init__(self ,name, age,salary):
# #             self.name=name
# #             self.age=age
# #             self.salary=salary


# # emp1=Employee('David',23,45000)
# # emp2=Employee('Esha',21,75000)
# # emp3=Employee('Rayan',23,200000)


def  square_result(fun):
    def inner_fun(*args):
        result=fun(*args) 
        return result*result
    return inner_fun


class calculator:
    @square_result
    def Add(self,*args): # here *args means to take all arguments as tuple 
        add=0
        for num in args: # here args means that u have a tuple on which u need to perfrom operations 
            add=add+num
        return add
    
    @square_result
    def Muntiply(self,*args):
        muntiply=1
        for num in args:
            muntiply=muntiply*num
        return muntiply
    

obj1=calculator()
print('Square of add ',obj1.Add(2,4,5))
print('Square of muntiply ',obj1.Muntiply(2,6))

# # dictionary = {}


# # def memoize(fun):
# #     global dictionary

# #     def inner_fun(*args):
# #         if args not in dictionary:
# #             dictionary[args] = fun(*args)
# #         return dictionary[args]

# #     return inner_fun


# # @memoize
# # def fibonacci(num):
# #     if num == 0:
# #         return []
# #     elif num == 1:
# #         return [0]
# #     elif num == 2:
# #         return [0, 1]
# #     else:
# #         result = [0, 1]
# #         for i in range(2, num):
# #             result.append(result[-1] + result[-2])
# #         return result


# # def factorial(num):
# #     if num == 0:
# #         return 1
# #     else:
# #         return num * factorial(num - 1)


# # option = 1
# # while option != 0:
# #     numbers = int(input('''Enter the number for which you want to calculate the 
# # fibonacci series and factorial: '''))
# #     print(f'The Fibonacci series of {numbers} is {fibonacci(numbers)}')
# #     print(f'The factorial of {numbers} is {factorial(numbers)}')
# #     option = int(input('Enter 1 to again check the Fibonacci series:\nEnter 0 to exit: '))

# dictionary={}

# def memoize(fun):
#     def inner(*args ):
#         dictionary[args]=fun(*args)
#         return dictionary[args]
#     return inner

# @memoize
# def fibonacchi(num):
#     recursion=[]
#     if num==0:
#         return []
#     elif num ==1 :
#         return[0]
#     elif num ==2:
#         return [0,1]
#     else :
#         recursion = fibonacchi(num-1)
#         recursion.append(recursion[-2]+fibonacchi(num-1)[-1])
#     return  recursion

# @memoize
# def factorial(num):
#     if num==0:
#         return 1 
#     else :
#         return  num * factorial(num-1)
    

# option=1
# while  option != 0:
#     choice_fun=int(input('Enter 299 for fibonachii \nEnter 399 for  factorial : '))
#     if choice_fun == 299:
#         number=int(input('Enter a number to calculate the fibonacchi series : '))
#         print(f'The fibonachii series of {number} is {fibonacchi(number)}')

#     elif choice_fun == 399 : 
#         number=int(input('Enter a number to calculate the factorial : '))
#         print(f'The factorial of {number} is {factorial(number)}')

#     option=int(input('Enter 0 to exit \nEnter 1 to continue \nEnter 2 to get all the previous rezult : '))

#     if option == 0 : 
#         print('Exit : ')
#     elif option == 2 :
#         print(dictionary)