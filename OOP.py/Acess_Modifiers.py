# There are 3 types of  acess modifiers in python :
# 1 . public 
# 2 . private
# 3 . protected

# 1 : public : 
# All the variable/Attributes function/Methods are by default public meaning u can use them  where u want 
# 2 : private 
# private acess modifer make the varible / method only avalible for  the class they are currenty in present 
# You can only make the variable private using the __ written with the variable e.g.(__variable)
# 3 : protected
# Protected acess  modifiers make the varible /  method  only  avalible for class and sub class

class Practice:
    __variable1=9 # private variable
    print('private varibale : ',__variable1) # output : 9
    _variable2=10
    print('protected varibale : ',_variable2) # output : 10

# class Practice2(Practice):
#     print('private varibale , Sub class : ',__variable1)
#     print('private varibale : ',_variable2)


obj=Practice()
# print(obj.__variable1)# Here as the variable is acessable outside of the class so  it  will  give  error
print(obj._variable2)# Here as the variable is acessable outside of the class so  it  will  give  error