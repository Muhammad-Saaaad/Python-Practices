# Exercise 1: Print Multiplication Table

print('Enter a number to find its table : ')
number=int(input())
for i in range(1,11):
    print(number,' * ',i,' = ',number*i)

# Exercise 2: Factorial Calculation    

no1 = int(input('Enter a number : ')) 
a=1
for i in range(no1,0,-1):
    a=a*i 
print('Factorial of ', no1 ,' is ',a)

# Exercise 3: Number Guessing Game

import random

i=0
takenumber=random.randint(1,100)

userdecide=int(input('Enter a number between 1 to 100 : '))

for i in range(10):
    if userdecide!=takenumber :   # game with using the for loop 
       i+=1
       if userdecide > takenumber:
           print('Too high : ')
       elif userdecide<takenumber:
           print('Too low : ')
    if userdecide==takenumber :
        print('U guess the correct number  :')
        break  
    userdecide=int(input('Enter a number between 1 to 100 : '))    
print('U have taken ', i , 'No of attempts : ')

# #Exercise 4: Print Diamond Pattern

b=0
for i in range(5):
    b+=1   # only this why we can do incrementation 
    for j in range(5-i,0,-1):
        print('', end=(' '))
    for k in range(b):
        print('*',end=('*'))
    print('\n')

for i in range(5):
    for k in range(i+1):
        print('',end=' ')
    for j in range(5-i):
        print('*', end='*')
    print('\n')

# Exercise 1: Print Even Numbers

for i in range(1,21):
    if(i%2==0):
        print(i, ' is even number : ')
i=2
while(i%2==0 and i<=20):
    print(i, ' is even number ... : ')
    i+=2    

# Exercise 2: Reverse a String 

name=input('Enter a name : ')
length=len(name)                # hard method
j=length-1
for i in name :
    print(name[j])
    j-=1

name=input('Enter name : ')
i=len(name)-1
while(i>=0):
    print(name[i])
    i-=1

# Exercise 4: Palindrome Check

name = input('Enter name : ')
i=len(name)-1
j=0
k=0
while i>=0:
    if name[i]==name[j]:
        k+=1
    else:
        k-=1
    i-=1
    j+=1
if k==len(name):
    print(name , ' is palindrome : ')
else:
    print(name , 'is not palindrome : ')    

# Exercise 5: FizzBuzz

for i in range(1,101):
    if i%3==0:
        print(i , ' is Fizz : ')
    if i%5==0 :
        print(i , ' is Buzz : ')   
    if i%3==0 and i%5==0 :
        print(i , ' is FizzBuzz : ')

# Exercise 6: Pattern Printing

for i in range(10):
    for j in range(i):
        print('*',end='')
    print('\n')    

# Exercise 7: Prime Number Check    

no=int(input('Enter a number : '))
j=0
for i in range(1,no+1):

    if no%i==0 :
        j=j+1
if j==2:
    print(no , ' is prime : ')
else :
    print(no , ' is not prime : ')

# Question 1: Fibonacci Series

no=int(input('Enter a number : '))
i=0
a=0
b=1
c=0
print('Fibonachii sequence is : ')
while a <=no:
    print(a)
    a=c+b
    c=b
    b=a   

# Question 4: Anagram Check :

name1=input('Enter name1 : ')
name2=input('Enter name2 : ')

if len(name1)==len(name2):
    k=0
    for i in name1:
        for j in name2:
            if i==j :
                k+=1
                #print(k)
                break
    if k==len(name1):
        print('Both names are Anagram Check : ')
    else :
         print('Both names are not Anagram Check : ')    
else :
    print('Both names are not Anagram Check : ')

# Question 6: Decimal to Binary Conversion

d_no=int(input('Enter a decimal number : '))
for i in range(d_no,0,-1):
    saving_no=str(d_no%2)
    print(saving_no,end='')
    if d_no/2<=0:
       break
    d_no=int(d_no/2)