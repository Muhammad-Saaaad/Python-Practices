# Calculator without input

# a=10
# b=2 

# print('Addation = ',a+b)
# print('Substraction = ',a-b)
# print('Muntiplication = ',a*b)
# print('division = ',a/b)
# print('Moduls = ',a%b)
# print('Float division = ',a//b)
# print('Expontentional operator = ',a**b)

# Calculator using input 

    # input() return value into String 
    # To perform Mathmetical operations we use type casting must 

choice='yes'

while(choice=='yes'):
    a=input('Enter 1st number : ')
    b=input('Enter 2nd number : ')
    op=input('Enter operator : ')
    match op:
        case '+':
            print('Add = ',int(a)+int(b))
        case '-':
            print('Substraction = ',int(a)-int(b))
        case '*':
            print('Muntiplication = ',int(a)*int(b))
        case '/':
            print('division = ',float(a)/float(b))
        case '%':
            print('Moduls = ',float(a)%float(b))
        case '//':
            print('Float division = ',int(a)//int(b))
        case '**':
            print('Expontentional operator = ',int(a)**int(b))
        case _:
           print(ord('B'),'invalid operator ') # type casting 

    choice=input('Enter yes to restart and no to exit : ')  
else:
    print('Program exit : ')               