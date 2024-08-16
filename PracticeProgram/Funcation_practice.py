#Question 1: Default Arguments
# Write a function called greet that takes a person's name as an argument and prints a greeting message.
# The function should have a default value for the name argument, so if no name is provided, it should 
# print a generic greeting.

def greet(name='default'):
    if name:
        print('Greeting ',name)
    else:
        print('Greeting sir :  ',name )
        
Name=input('Enter name : ')     
greet(Name)   
# def greet(name='sir'):
#     if name != 'sir':
#         print('Greetings, ' + name + '!')
#     else:
#         print('Greetings, sir!')

# Name = input('Enter name: ')
# greet(Name)



# Question 2: Keyword Arguments
# Write a function called calculate_total that takes the price and quantity of a product as arguments
# and calculates the total cost. The function should accept the arguments using keyword arguments,
# allowing the caller to pass the arguments in any order.

def calculate_total(price , quantity):
    print('Total cost = ',price*quantity)

calculate_total(quantity=2,price=120)    

# Question 3: Variable Number of Arguments
# Write a function called average that takes any number of arguments and returns the average of those numbers. 
# The function should handle both integer and floating-point arguments.

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print('Average = ',sum/len(numbers))    

average(23,42,12,4,2,31,1)


# Question 4: *args and **kwargs
# Write a function called print_info that accepts a person's name, age, and any additional information as 
# keyword arguments. The additional information can vary, so the function should accept any number of keyword
# arguments. The function should print the person's name, age, and other provided information.

def print_info(**info):
    print(info['name'],info['age'],info['adress'])

print_info(name='David',age=18,adress='street no 7')


# Question 5: Recursive Function
# Write a recursive function called factorial that calculates and returns the factorial of a given number. 
# The factorial of a number is the product of all positive integers up to and including that number.

def factorial(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac 

num=int(input('Enter a number : '))

print('Factorial of ',num,' is',factorial(num))


# Question 6: Callback Function
# Write a function called apply_operation that takes two numbers and a callback function as arguments.
# The function should apply the callback function to the two numbers and return the result. 
# The callback function should perform a specific mathematical operation, such as addition, subtraction, multiplication, or division.

def callback():
    operator=input('Enter an mathmetical operator : ')
    return operator

def apply_operation(a,b,c):
    match c:
        case '+':
            print('sum = ',a+b)
        case '-':
            print('Sub = ',a-b)
        case '*':
            print('Muntiply = ',a*b)
        case '/':
            print('Divide = ',a/b)

num1=int(input('Enter a number : '))
num2=int(input('Enter a number : '))
apply_operation(num1,num2,callback())