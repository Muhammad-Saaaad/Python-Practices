# a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly
#  used as arguments to higher-order functions, such as map, filter, and reduce.

square = lambda x : x*2
print('Square : ',square(2))
avg=lambda a,b,c,d : (a+b+c+d)/4
print('Average : ',avg(1,2,3,4))

def use_of_lambda(fun,v1,v2,v3,v4):
    return 10+fun(v1,v2,v3,v4)

print('lambda functions as an argument : 1 ',use_of_lambda(avg,3,6,5,7))
# or use can simply type the lambda function as an argument  
print('lambda functions as an argument : 2 ',use_of_lambda(lambda a,b,c,d : (a+b+c+d)/4, 3,6,5,7 ))