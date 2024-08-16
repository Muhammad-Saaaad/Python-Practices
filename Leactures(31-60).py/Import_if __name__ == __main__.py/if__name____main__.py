# The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run
# directly or being imported as a module into another script.

# Let's break it down :
# __name__ , when the code contaning __name__ is run , main is Stored in the __name__  and the code Written it the if __name__ == "__main__" 
# is executed , and when we import the module into another module the code written in the if __name__ == "__main__" is not exexcuted as 
# the __name__ contains the name of the module and if __name__ == "__main__" return false and is not executed .

# This is very important to do so as when u import a module all the code in the module is executed , and if write if __name__ == "__main__" 
# , all the code will will be executed except the code written in the if __name__ == "__main__" . 

def fun():
    print('code inside the function : ')

print('code freely existing : ')

if __name__=="__main__":
    print('code inside the if __name__=="__main__": ')
    print(__name__)

# when we run the code on some other file we get this : 

# import if__name____main__ as imp_mod

# imp_mod.fun()   # output: code inside the function : 
# print(imp_mod.__name__)  # output:  if__name____main__