# Function is use to re-write  our code again and again without writing the whole logic everytime : 

def table(a,b):
    for i in range(1,11):    # If the is Returntype void 
        print(a,'*',i,'=',a*i ,'  ',b,'*',i,'=',b*i)

def add10(a):               # If the Returntype is int 
    return a+10

table(2,3) 
b=10
print(add10(b))

# To acess the globle variable into the funcation use keyword global 
color='no color '
def updatecolor(c='yellow'):
    global color       # you cannot drictely give the value here 
    color=c
    print(color)
updatecolor()

# Types of Arguments in a funcation : 

 # 1: Default Arguments
 # Default Arguments are those arguments which are provided by the value when creating function 
 # the default argument only works when u do not provide a value to a funcation argument 
def fun(a=10 , b=9):
    print('sum is ',a+b)# Here a , b are default Arguments
# You can provide the arguments to a function in these all follwing ways     
fun()#Here if we don't provide the arguments it will use the default values 
fun(3)# here it will take 3 as the value of a and the value of b is taken as default 
fun(b=3)# here it will take the value of b and the value of a is taken as default 
fun(a=4,b=2)
fun(4,2)

 # 2: Keyword Arguments 
 # if u want not to pass the arugments in an order then u can use the keyword arguments 
 # you only need to pass the value with the argument name (that name that is use in the function parameters )

def name(fname , midname , lname):
    print(fname,midname,lname)

name(midname='vin',fname='lara' , lname='daz') # keyword arguments 

 # 3: Required Arguments 
 # Those Arguments that are not the default arguments are called Required Arguments 
 # if you do not provide the value to an arguments not by keyvalue and it is not default argument then it will be know as required argument

def example(a,b,c=3):
    print('sum is : ',a+b+c)

example(1,2,4)    # here 1 and 2 are requied arguments 

 # 4: Variable Length argument 
 # Sometimes we need to pass more variable then the varibales define in the funcation argument so we use variable length argument 
 # There are 2 ways to achieve this :

   # a: Arbitiary Arguments 
   # To achieve this , simply pass the * before the name of the parameter so that the function will take all the values in form of tuple

def arbitiary(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers: # as the numbers here is pass in the form of tuples so we won't use the range function 
        sum=sum+i
    print('The sum of numbers are : ', sum ) 
    print(numbers) 

arbitiary(1,2,3,4,5)   

   # b: Keyword Arbitiary Arguments
   # To achieve this type , simply pass ** before the name of the parameter so that the function will take all the values in form of dictionary

def keyword_Arbitiary(**name):  # Here the name passed is in the form of dictionary 
    print(type(name))  # you can check the type of the parameter using type() funcation 
    print(name)
    print('dictionary = ',name['age'],name['name'],name['degree'])

keyword_Arbitiary(name='Saad',age=18,degree='BSCS')    