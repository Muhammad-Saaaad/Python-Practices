# # making list 
# listing=[1,'abc',2.32]
# print(listing[0])

# # making distionaries 
# dis={'Name':'saad','age':2,'DOB':'2004-10-6'} # distionaries has a key and a value 
# print('Discitionary ',dis['DOB'])
# # add key and a value # Modifing values
# dis['Gender']='male'
# dis['age']=18
# print('Discitionary ',dis)

# # String indexing and Slicing 

# word='My name is Muhammad Saad '
# print(word[4]) # indexing 
# print(word[3:10]) # Slicing 

# # Step size

# word='My name is Muhammad Saad '
# print('Step size ', word[::2])
# # we can also do reverse the String using Step Size 
# print('reverse String ',word[::-1])

# # Type Casting 

# number = '1002'
# print(float(number))

# # Taking Input
# b=2
# no1=input("Enter a number :")

# print("Number is ",no1)

# print('M = ',ord('M'),' S = ',ord('S'))

# def name(n):
#     length=len(n)
#     l=-1
#     k=0
#     for i in range(int(length/2)):
#         if n[i]==n[l]:
#             k+=1
#             l-=1
#     if k==int(length/2):
#         return True 
#     else :
#         return False

# Value=input('Enter a name : ')

# if name(Value)==True:
#     print(Value ,' is palandrom : ')
# else :
#     print(Value ,' is not palandrom : ')

# Implement a function to check if a given number is a prime number.

# def prime(n):
#     f=0
#     for i in range(2,n):
#         if n%i==0:
#             f+=1
#     if f>0:
#         return False
#     else :
#         return True  
        
# no=int(input('Enter a number : '))
# if prime(no)==True:
#     print(" The number is prime : ")
# elif prime(no)== False :
#     print(' THe number is not a prime : ')

# Given a list of integers, find the longest increasing subsequence (non-contiguous) within the list

# def subsequence(lists):
#     '''This funcation takes a list and return a sub sequence of it '''

#     lists.sort()
#     list_save=[]
#     length=len(lists)
#     for i in range(length-1):
#         if lists[i+1]-1 == lists[i]:
#             list_save.append(lists[i])
#             list_save.append(lists[i+1])
#     for i in range(len(list_save)):
#         if i == len(list_save)-1:
#             break
#         if list_save[i]==list_save[i+1]:
#             list_save.remove(list_save[i])
#     return list_save

# print(subsequence([1,2,3,23,21,423,32,53,12,321,67]))
# print(subsequence.__doc__)

# Write a program to solve the Tower of Hanoi problem with n disks.

# def Hanoi (n)