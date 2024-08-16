# There are 2 types of variables : 
# 1 : local varibale and global variable : 
x=3 # Global variable 

def fun():
    y=9 #local variable
    # TO acess the globale variable inside of function we use the keyword : 
    global x 
    x=5
    # if we don't use the keyword global then it will consider another x that will be local  :
    # so know we will have 2 x one is local and one will be global and hence it will make the readability of our program poor :      
