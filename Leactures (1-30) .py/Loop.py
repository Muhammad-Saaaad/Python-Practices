# For loop 
 # the For loop use a Funcation range() , that is use for initalization , range and increment 
 # Generally the initalization that starts from 0 and it is by default and the increment of 1 is also by default 
 # for loops cannot contain any condation and the range function is only executed once

for i in range(0,10,2):  # 0 is for the initalization , 10 is for the condation , 2 is for the increment 
    if(i<5):
        print(i , 'is less then 5 ')
    else:
        print(i)    

# you can zip() funcation to take 2 values at a time in for loop:
  # but u cannot pass integer values : // only iterateable values 
for i , j in zip('ali','saad'):
    print('zip() : ',i,j)

# to rake value into integer use this : 
for i , j in zip(range(5),range(6)):
    print('zip() int: ',i,j)

# we can also use for loop for String as :
name = 'saad'
for i in name : # here the 1st index is pas sed to the i and then 2nd and so on 
    print(i)

# we can also do this for List 
mylist=['saad','umaz','ibrahaim','zakriya']
for i in mylist:
    print(i)

# While Loop 
#  The Syntax of WHile loop is excatly the same as While Loop in c++ and c 
i=0
while(i<=10):
    print(i)
    i+=1   
# do-While Loop :
#  There is no do_while loop in python : but if u want to make a do-while loop then 
a=input('Enter a name : ')   #In this way we can use while loop to make a do-while loop 
while(a!='Hamza'):           # Simply write a statment in the While loop and re-write all those statments above the while loop to make a do-while loop 
    a=input('Enter a name : ')    
else:
    print('name is hamza : ')    # you can also use else with the While loop 

# Or you can make do-while by follwoing method :

i=0
while True:
    print(i)
    i+=1
    if i>10:
        break

# you can also use else with the for loop

for i in range(5):
    print(i)
else :    # else means if the condation becomes false as in this case when i becomes 5 it will retrun false and the else will be executed 
    print('loopbreaks')