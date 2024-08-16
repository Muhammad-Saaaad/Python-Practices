# if_else 
 # we don't really need to add parameters with the condation 
  # write a program to input 3 numbers from user and display the greater number 

no1=int(input('Enter 1st number : '))
no2=int(input('Enter 2nd number : '))
no3=int(input('Enter 3rd number : '))

if no1>no2 and no1>no3:
     print('The greatest number is : ', no1)   # THE LOGICAL OPERATOR WE USE THE FULL NAME ('and','or','not') 
elif(no2>no1 and no2>no3):
     print('The greatest number is : ', no2) 
elif no3>no1 and no3>no2:
     print('The greatest number is : ', no3)   
else:
     print('All numbers are Equal : ') 

# Match Case 
#  OR u can call it SWITCH CASE 
           
  # maing a calculator using Match / Switch case 
  # In Python, there is a keyword called ( match ) is use instead of keyword ( switch  ),
  # there is no break statment , 
  # and in default case we just write underscore( _ ) at the place of default keyword

no1=float(input('Enter no 1 '))
no2=float(input('Enter no 2 '))
operator=input('Enter opeartor ')
match operator:
     case '+':
          print('Addation : ',(no1+no2))
     case '-':
          print('Substraction  : ',(no1-no2))
     case '*':
          print('Muntiplication : '(no1*no2))
     case '/':
          print('Division : ',(no1/no2))
     case '%':
          print('Modulus : ',(no1/no2))
     case _ if operator == '!':
          print(" ! is an Invalid operator : ")
     case _:
          print('Invalid operator : ')