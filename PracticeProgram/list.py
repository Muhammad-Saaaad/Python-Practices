# l=[1,2,3,1,1,4,5,1,2,2,6,4,3,7,8]
# m=list(set(l))
# print(m)

# def slicing(Strings,length):
#     long_strings = [string for string in Strings if len(string) > length]
#     return long_strings

# String_list=[]
# print('Enter 5 names : ')
# for i in range(5):
#     a=input()
#     String_list.append(a)  
# length=int(input('Enter length of a Single String for output : '))
# print('list of String having length > ',length,slicing(String_list,length))  

# def concate(list1,list2):
#     return(list1+list2)
# list1=[]
# list2=[]       # without using the append funcation whatever u input it will rewrite that and also it will take 'saad' as 's','a','a','d'
# for i in range(3):
#     list1.append(int(input('Enter a number : ')))
#     list2.append(int(input('Enter a number : ')))

# print(concate(list1,list2))    


# list1=[]
# print('Enter any 10 numbers : ')
# for i in range(10):
#     list1.append(int(input()))

# list2=[i for i in list1 if i%2==0]   
# print('even numbers in list : ', list2) 

# li=[]
# print('Enter 5 names : ')
# for i in range(5):
#     li.append(input())

# li.sort()  # In list sorting is on the base of length :
# print(li)

# list1=[1,2,3,4,2]
# target=2

# def search(list1, target):
#     if target in list1:
#         return -1 
#     else:
#         print('not found : ')

# print(search(list1,target))     

# def list_operations(list1):
#     sum=0
#     for i in list1:
#         sum=sum+i
#     print('sum : ',sum)   

#     for i in list1:
#         k=0
#         for j in list1:
#             if i<j:
#                 continue
#             else:
#                 k+=1     
#         if k==len(list1):
#             print(i ,'is the maximum number : ')

#     for i in list1:
#         k=0
#         for j in list1:
#             if i>j:
#                 continue
#             else:
#                 k+=1
#         if k==len(list1):
#             print(i ,'is the minimum number : ')
#     list1.sort(reverse=True)
#     print('Sorting in decending : ',list1)
#     print('Average of numbers in the list : ',sum/len(list1))


# list_operations([7,1,5,8,8])                


# Find the maximum and minimum number in the list : 
# listing=[]
# print('Enter 10 numbers in the list :')
# for i in range(10):
#     number=int(input('Enter a number : '))
#     listing.append(number)

# maximum=minimum=listing[0]
# for i in listing:
#     if i>maximum:
#         maximum=i
#     elif i<minimum:
#         minimum=i

# print(f'Maximum number is : {maximum}')
# print(f'Minimum number is : {minimum}')

# def sum(arr):
#     s=0
#     for i in arr:
#         s=s+i

#     return s

# def avg(arr):
#     s=sum(arr)
#     return s/len(arr)

# def product(arr):
#     p=1
#     for i in  arr:
#         p=p*i
#     return p

# arr=[]
# for i in range(10):
#     arr.append(int(input(f'Enter number {i+1 }')))

# print('list : ',arr)
# print('sum : ',sum(arr))
# print('Average : ',avg(arr))
# print('product : ',product(arr))

# # Matrix Operations: Write functions to add, subtract, and multiply two matrices.

# M1=[[1,2,3],[4,5,6],[7,8,9]]
# M2=[[23,89,76],[84,45,12],[12,54,65]]

# def add(a1,a2):
#     M3=[]
#     for i in range(3):
#         for j in range(3):
#             sum=a1[i][j]+a2[i][j]
#             M3.append(sum)

#     return M3

# def subtract(a1,a2):
#     M3=[]
#     for i in range(3):
#         for j in range(3):
#             sub=a1[i][j]-a2[i][j]
#             M3.append(sub)

#     return M3

# def multiply(a1,a2):
#     M3=[]
#     for i in range(3):
#         for j in range(3):
#             product=a1[i][j]*a2[i][j]
#             M3.append(product)

#     return M3


# def divide(a1,a2):
#     M3=[]
#     for i in range(3):
#         for j in range(3):
#             division=a1[i][j]/a2[i][j]
#             M3.append(division)

#     return M3

# print('Add : ',add(M1,M2))
# print('Subtract : ',subtract(M1,M2))
# print('Multiply : ',multiply(M1,M2))
# print('Divide : ',divide(M1,M2))

# Unique Elements: Write a function that takes an array and returns a new array with only the unique elements (no duplicates).

# listing=[1,34,45,2,1,45,2,34,4,21,45,1,0.35423,5]

# def unique(num):
#     s=set(num)
#     s=list(s)
#     return s

# print('before unique : ',listing)
# print('uniue is : ',unique(listing))

# Anagram Check: Write a function that checks if two strings are anagrams (contain the same characters in a different order).


# def Anagram(String1,String2):
#     log=0
#     if len(String1)==len(String2):
#         for i in String1:
#             if i in String2:
#                 log+=1
#         if log==len(String2):
#             return True
#     else :
#         return False
    
# s1=input('Enter a String ')
# s2=input('Enter a String ')
# print('Anagram Check : ',Anagram(s1,s2))

# Word Frequency Counter: Write a program that takes a text file as input and outputs the frequency of each word in the file.


    