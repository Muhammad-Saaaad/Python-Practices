# Reverse indexing : 
# sentence = input('Enter a String : ')
# sentence=sentence[::-1]
# print(sentence)
# integer=123                              # Int 
# #Str
# integer_convert_String=str(integer)
# print(type(integer_convert_String),integer_convert_String)
# #float
# integer_convert_float=float(integer)
# print(type(integer_convert_float),integer_convert_float)
# #list
# # integer_convert_list=list(integer)
# # print(type(integer_convert_list),integer_convert_list)
# # you cannot convert a integer drictly into list rather u need to do this :
# # to make a integer into a list we use the combination of integer and String 
# integer_list=[i for i in str(integer)]
# print(type(integer_list),integer_list)
# # Set:
# # integer_set=set(integer)
# integer_set={i for i in  str(integer)}
# print(type(integer_set),integer_set)
# #Tuple:
# integer_tuple=(i for i in str(integer))
# print(type(integer_tuple),integer_tuple)
# # Dictionary:
# # Dictionary is make when we have keys and values 

# String='12345'                        # String 
# # int
# integer=int(String)
# print(type(integer),integer)
# #Float
# floating=float(String)
# print(type(floating),floating)
# #list
# listing=list(String)  # you can drictly make the list into the String 
# print(type(listing),listing) 
# #tuple
# tupling=tuple(String)
# print(type(tupling),tupling)
# #set
# seting=set(String)
# print(type(seting),seting)

# floating=145.9                       # Float
# #int
# integer=int(floating)
# print(type(integer),integer)
# #string
# String=str(floating)
# print(type(String),String)
# #list 
# listing=[i for i in str(floating)]
# print(type(listing),listing)
# #Tuple
# tupling=tuple(String)
# print(type(tupling),tupling)

# listing=['1','2','3']                #list 
# # to convert a list into integer 1st convert the list into String using list conversion and then convert the String into list 
# #int and String
# String=''.join(str(i) for i in listing)
# print(type(String),String)
# integer=int(String)
# print(type(integer),integer)

# # float
# # same as the integer 
# String=''.join(str(i) for i in listing)
# floating=float(String)
# print(type(floating),floating)
# #tuple 
# tupling=tuple(listing)
# print(type(tupling),tupling)
# #set 
# seting=set(listing)
# print(type(seting),seting)

# tuple=(1,2,3,4,5)                # Tuple 
# integer=''.join(str(i) for i in tuple)
# print(type(int(integer)),int(integer))
# #list
# listing=list(tuple)
# print(listing)

# # one thing that u need to rembember is that : 
# # to convert a list into String use join method with list compresentation : 
# # String=''.join(i for i in str(listing)) if u apply String here then it will convert each elemnet of the list into a String 
# String=''.join(str(i) for i in listing)
# print(type(String),String)
# print('to convert a String into a integer : ',int(String))

# s1=input('Enter sentence : ')
# s2=input('Enter sentence : ')
# s=[]
# for i , j in zip(s1,s2):
#     s.append(i)
#     s.append(j)
# s=''.join(i for i in s)
# print(s)

# words_list=['a','b','c',' ','g']
# String=''
# for i in words_list:
#     if i!=' ':
#         String=String+i
#     else:
#         break
# print(String)

