# # Enumerate function is a built in funcation in python programming that is use to return a tuple that consist of index and the value of that 
# # index . only the iterate able value can be pass to a Enumerate function 

# # Syntax : 

# # Enumerate function returns the value in a tuple that if we pass 2 variables then the tuple will dislocate itself as give its both values to 
# # each of the variable
# listing=['Apple','Banana','Mango']
# for v in enumerate(listing):
#     print(type(v),v)

# # String 

# String ='Hello world'
# for i,j in enumerate(String):
#     print(type(i),i ,' ',type(j),j) # when the tuple is dislocated then the value pass to the variables will be in there orignal form 

# # list

# listing=['Apple','Banana','Mango']
# for index , value in enumerate(listing):
#     print(index,' ', value)

# # Set 

# seting={'Water melon','Peach','Orange'}
# for index , value in enumerate(seting):  # hence set will also work but the position of indexes will not be always the same 
#     print(index,' ', value)  # rembember the position of index is not always the same 

# # Tuple 

# tupling=(76,98,100,101)
# for i , j in enumerate(tupling):
#     print(i ,' ',j)

# # Dictionaries : 

# Dictionary={'Key 1 ':32,'Key 2':46,'Key 3':69}
#  # As we know that in the dictionary , the key 1 and 32 are on the 1st index as similary key 2 and 46 are on the 2nd index and so on...
#  # so it will acess the index no and the key because if it acess the key then we will be able to acess the value of that key as well 
# for index , value in enumerate(Dictionary):
#     print(index,' ', value)  

# # Create a dictionary  :
# listing=['value 1 ','value 2','value 3']
# Dictionary1={}
# for index , value in enumerate(listing):
#     Dictionary1[index]=value
# print(Dictionary1)



# Write a Python function that takes a list of names as input and returns a dictionary where the keys are the names, and the values are their corresponding indices (starting from 1).

# def enu(lis):
#     dic={}
#     for value  , name in enumerate(lis , start=1):
#         dic[name]=value
#     return dic

# name_list=['saad','Ali','Harry','Moiz','Obaid']

# print(enu(name_list))


# Write a Python program to find all the prime numbers in a given list of integers. Use the enumerate function to print the prime numbers along with their indices.

# def find_prime(p):
#     for  index , prime in enumerate(p):
#         a=0
#         for  i  in range(2,prime):
#             if  prime%i==0:
#                 a=1
#                 break
#         if  a == 0:
#             print(prime ,' is the prime number having index : ',index)

# integer_list=[2,5,7,54,6,7,254,8,9,3,89,54,87,54,8,25,4,84,524]

# find_prime(integer_list)

# Given a list of words, use the enumerate function to create a new list of tuples where each tuple contains the word and its length.

# def words(w):
#     tuple_list=[]
#     for index , word in enumerate(w):
#         t=[]
#         t.append(word)
#         t.append(len(word))
#         tuple_list.append(tuple(t))

#     return tuple_list

# print(words(['saad','ali','Ahmed']))


# Question :
# def unknown(sentence):
#     sentence_list=sentence.split(' ')
#     word_dict ={}
#     for index , value in enumerate(sentence_list):
#         if value in word_dict :
#             word_dict [value].append(index) # here as the index is  being stored as list so we can also append that list
#         else :
#             word_dict [value]=[index] # here we make the value Stored on the behafe of key is as list
#     return word_dict 



# sentence='hi my name is unknownpg and this  here also has name unknownpg'
# print(unknown(sentence)


# You are given a list of temperatures in Celsius. Write a program to convert each temperature to Fahrenheit using the formula
#  (Celsius * 9/5) + 32. Use the enumerate function to print the Fahrenheit temperatures along with their corresponding indices.

# def temp_convert(temp):
#     farhenhiet=[]
#     for index,celcius in enumerate(temp):
#         farhenhiet.append(((celcius * 9/5)+32,index))
#     return farhenhiet

# print(temp_convert(temp=[34,43,32,29,100,0+0]))


# def find_sum(num,target_sum):
#     lis=[]
#     for index1 ,num1 in enumerate(num):
#         for index2 , num2 in enumerate(num[index1 +1:] , start=index1 +1):
#             if num1+num2  == target_sum:
#                 lis.append(((index1, index2),(num1,num2)))
#     return lis


# Create a function that takes a list of words and returns a new list of words with their vowels capitalized. Use the enumerate function 
# to process the characters of each word.

# def transform_words(words_list):
#     wovels=['a','e','i','o','u']
#     vowel_words_list=[]
#     for index1 , word in enumerate(words_list):
#         alphabet_list=[]
#         for index2 , alphabet in enumerate(word):
#             if alphabet.lower() in wovels:
#                 alphabet_list.append(alphabet.upper())
#             else:
#                 alphabet_list.append(alphabet)
#         capital_word_alphabet=''.join(i for i in alphabet_list)
#         vowel_words_list.append(capital_word_alphabet)
    
#     return vowel_words_list

# print(transform_words(words_list=['hello',  'there', 'my', 'name' ,'is' ,'unknownpg']))

# You are given a list of names. Write a Python program to find the longest name using the enumerate function.

def longest_name(name_list):
    return_name=''
    index_of_name=0
    for index , name in enumerate(name_list):
        if len(name) > len(return_name):
            return_name=name
            index_of_name=index
    
    return (return_name , index_of_name)

print(longest_name(['saad','ali','hamza','ahmed','umer','unknownpg']))
