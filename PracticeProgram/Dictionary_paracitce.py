# practice : 
 # Given a list of dictionaries, each representing a student with their name and score, write a program to find the student with the 
 # highest score.

# max_marks={}

# for i in range(2):
#     option_k=int(input('Enter 1 for integer key \nEnter 2 for String key : '))
#     option_v=int(input('Enter 1 for integer value \nEnter 2 for String value : '))
#     if option_k==2:
#         key=input('Enter the key : ')
#     elif option_k==1:
#         key=int(input('Enter the key : '))
#     if option_v==2:
#         value=input('Enter the value : ')
#     elif option_v==1:
#         value=int(input('Enter the value : '))
#     max_marks[key]=value


# li=list(max_marks.keys())
# for i in li:
#     k=0
#     for j in li:
#         if max_marks[i]>=max_marks[j]:
#             k+=1
#     if k==len(li):
#         print(max_marks[i],' has the highest value : ')
#         break

# Write a Python program to count the frequency of each element in a list and store the results in a dictionary.

# _list=[]
# for i in range(10):
#     no=int(input('Enter a number : '))
#     _list.append(no)
# frequency={}
# for i in _list:
#     value=_list.count(i)
#     frequency[i]=value

# print(frequency)

# Implement a function to merge two dictionaries into a single dictionary, with the values of common keys appended together.

# dic1={}
# for i in range(5):
#     key=input('Enter a key : ')
#     Value=int(input('Enter a value : '))
#     dic1[key]=Value

# dic2={}
# for i in range(5):
#     key=input('Enter a key : ')
#     Value=int(input('Enter a value : '))
#     dic2[key]=Value

# print('dictionary 1 ',dic1)
# print('dictionary 2 ',dic2)

# dic1.update(dic2)
# print('dictionary after merging ',dic1)

# Given a list of strings, create a dictionary where the keys are the strings, and the values are the lengths of the strings.

# list_s=[]
# for i in range(5):
#     name=input('Enter name : ')
#     list_s.append(name)
# dic_s={}
# for i in list_s:
#     length=len(i)
#     dic_s[i]=length

# print(dic_s)

# Write a function to check if a given key exists in a dictionary.

# name={'saad':4,'Ali':3,'hamza':5,'help':4}
# given_name=input('Enter a key to check if its exist or not : ')
# for i in name.keys() :
#     if i==given_name:
#         print('the Key exist : ')
#         break

# Implement a program to remove duplicate values from a dictionary.

# name={'saad':4,'Ali':3,'hamza':5,'help':4,'saadi':4,'abc':3}

# def no_duplicate(unique):
#     dis={}
#     l=[]
#     for key , value in unique.items():
#         if value not in l:
#             l.append(value)
#             dis[key]=value
#     return dis 


# print('result without any duplication is : ',no_duplicate(name))

# Implement a program to remove duplicate values from a list.

# def list_recursion(list_name):
#     s=set(list_name)
#     s=list(s)
#     return s

# print(list_recursion([1,2,3,1,2,3,1,6,3,2,6,3,5,4,5,4]))

# Given two dictionaries, write a function to find the common keys and their corresponding values between the two dictionaries.

# def two_dictionaries(dic1,dic2):
#     if len(dic1)==len(dic2):

#         for i in dic1.keys():
#             for j in dic2.keys():
#                 if i==j:
#                     print(i ,' and ', j ,'are the same ')
#                     print('the value of ',i ,' is ',dic1[i])
#                     print('the value of ',j , ' is ',dic2[j])
#     else :
#         print('Invalid length ')

# two_dictionaries({1:1,2:2,3:3},{2:2,4:4,1:1})

# Write a program to sort a dictionary by its values in ascending order.
# def sort(dic):
#     return dict(sorted(dic.items() , key = lambda x:x[1]))

# print('Dictionary sort : ',sort({'saad':2,'Ali':1,'Harry':6,'pg':5})) 

# def sort_dictionary_keys(dictionary):
#     sorted_keys = sorted(dictionary.keys())
#     sorted_dict = {key: dictionary[key] for key in sorted_keys}
#     return sorted_dict

# # Test the program
# my_dict = {'key2': 'value2', 'key1': 'value1', 'key3': 'value3'}
# sorted_dict = sort_dictionary_keys(my_dict)
# print('Sorted Dictionary:', sorted_dict)


# # Implement a function to find the difference between two dictionaries (keys present in one but not the other).
# def diff_2dictionary(dic1,dic2):
#     s1=set(dic1.keys())
#     s2=set(dic2.keys())
#     same=s1.intersection(s2)
#     different=s1.symmetric_difference(s2)
#     print('The difference between both dictionaries are ')
#     print('Both have the Follwoing same keys : \n',same)
#     print('Both have the Follwoing differnet keys : \n',different)


# diff_2dictionary( {"name": "John","age": 25,"city": "New York","occupation": "Engineer"},
#  {"name": "Alice","age": 30,"country": "Canada","occupation": "Teacher"}
# )
# p_b={}
# condations='''Enter 1 : Add a new contact to the phone book
# Enter 2 :Update an existing contact's phone number.
# Enter 3 :Delete a contact from the phone book.
# Enter 4 :Search for a contact by name and display their phone number.
# Enter 5 :Display the entire phone book directory.
# Enter 6 :Exit.'''
# def phone_book():
#     op=0
#     while op!=9:
#         print(condations)
#         op=int(input())
#         match op:
#             case 1:
#                 add_new_contract()
#             case 2:
#                 update_contacct()
#             case 3:
#                 delete_contact()
#             case 4:
#                 search_contact()
#             case 5:
#                 display_full_Book()
#             case 6:
#                 print('Exit : ')


# def add_new_contract():
#     name=input('\nEnter name of your contract : \n')
#     phone_no=input('Enter your phone number : \n')
#     p_b[name]=phone_no
#     print('Contact Added : \n')

# def update_contacct():
#     name=input('\nEnter name of your contract which u want to update : \n')
#     phone_no=input('Enter your new phone number : \n')
#     p_b[name]=phone_no
#     print('Contact updated : \n')
    
# def delete_contact():
#     name=input('\nEnter name of your contract which you want to delete : \n')
#     del p_b[name]

# def search_contact():
#     name=input('\nEnter your name... \n')
#     print(name ,'  ', p_b.get(name),'\n')

# def display_full_Book():
#     for names,contacts in p_b.items():
#         print(names,'  ',contacts,'\n')

# phone_book()

# Question 1: Word Frequency Counter

# def word_frequency(sentence):
#     li=sentence.split(' ')
#     dic={}
#     a=0
#     for i in li:
#         dic[i]=a
#         a+=1      
#     return dic

# dic=word_frequency(input('Enter a sentence : '))
# print('Dictionary of the sentence is : \n',dic)

# Question 3: Duplicate Character Counter

# def character_counter(sentence):
#     li=list(sentence)
#     # print(li)
#     alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

#     dic={}
#     for j in alphabets:
#         c=li.count(j)
#         if c>0:
#             dic[j]=c
    
#     return dic
# print(character_counter(input('Enter a sentence : ')))