# Exception also called error that is occure when some unwanted process happens during the execution of program .
# to handle this we use Exception Handling 
  # Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).
  # When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled.
  # If not handled, the program will crash.

# In Excaption Handling we use try except blocks to handle if anything goes Wrong 

# Syntax :

# try:
#     a=int(input('Enter a value : ')) 
#     #  Suppose the user enter a String and then it will give and error and Stops but if we want to continue we will add an execpt :
#     #  execpt it use if the program in the try gives an error 
#     print(f'The square of {a} is : ',a*a)
#     b=[1,2,3,4]
#     print(f'value at {a} index is : ',b[a])
# except ValueError:      # here built-in Exception have different use like valueError for invalid value input and indexError for invalid index
#     print('you have enter the Wrong input : ')
#     # Enter a value : st
#     # you have enter the Wrong input :
# except IndexError: # you can use muntiple except . also you can avoid using buit-in Exception 
#     print('Number Written for index is out of range : ')


# # Finally :

# # The finally code block is also a part of exception Handling , use with the try except code blocks and is always execute irrespective 
# # of weather the condation is . Finally will always excute so it is generally used for doing the concluding tasks like closing file resources 
# # or closing database connection or may be ending the program execution with a delightful message..

# # The main work of Finally keyword is this .
# # Suppose you are making a funcation and there are some statments which you always want to b executed even the funcation returns value or not 

# def fun():
#     try:
#         a=[1,32,54,675,33]
#         i=int(input('Enter a value : '))
#         return a[i]
#     except :
#         print('invalid index :' )
#         return False
#     finally:
#         print('Finally Will always execute : ')
    
# print(fun())

# output:
# Enter a value : 1
# Finally Will always execute :  # here as you can see function is returing a value so techiquly Finlly will not have to execute but here 
# 32                         # first finlly is execute and then funtions returns a value means that no matter what finally will always execute
def fun():
    try:
        for i in range(5):
            if i == 3 :
                # print(i)
                print('anbdjasndkjasbndkuj')
                return True
    finally:
        print('application close : ')
        
print(fun())