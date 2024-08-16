my_dog=2 # In python there is no need to write data type with variables 

print(my_dog)

# Also a single variable can hold different data types : 

my_dog='ding dong  '

print(my_dog) # here it will pefer the closest datatype value (in this case it will get the print ) 
# output : ding dong 

a =3
print(type(a)) # if you want to get the datatype of a variable use the 'type()' function... 
int =43
print(int)

print("hello \n world " ) # \n escape sequence

print(len("im foody ")) # len() is a function that get the length of the string 

# indexing 

String = "hello world "

print(String[1])

# Slicing 

string='my name is saad '
print(string[3:]) # from index 3 to all the way to the end 

print(string[:4]) # from start to all the way to the index no 4 but don't include the index no 4 

print(string[4:10]) # from index no 4 to index no 10

# step size 

print(string[::2 ]) # print full String but jump at 2 indexs at a time  

print(string[1:10:3]) # go from 0 to 10 with the jump of 3

# reverseing the String using step size 

# print(string[::-1])

# if a<b :
#     print("hi")
#     if a<b:
#         print('k')

# for i in range(1 , 10 , 2):
#     print(i)

# i = 0
# while 