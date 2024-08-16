# In python the "is"  keyword is use to compare the location of 2 variables or memory of 2 variables where 
# "==" only compare the values of  2 variable , it does not compare the location of 2 variables 
   # Check deatils  in copy : 

a=[1,2,3]
b=[1,2,3]
print(a is b) # output : False : as both have the same value but different location because list are mutable 
print(a == b) # output : True : as both have the same value

a=(1,2,3)
b=(1,2,3)
print(a is b ) # output : True : as both have the same location because tuples are immutable
print(a == b ) # output : True : as both have the same  value 