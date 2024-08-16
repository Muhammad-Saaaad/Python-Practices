# sometimes the data in the if else is to short so we will use one hand if else statment
# In if 1st the statment will come and then the if condation 
# In else , 1st else comes and then the statment 
# if we want to make a elif , 1st else comes then the statment and then the if condation comes 
# Rembember else will always comes after the if no matters what
A=314
B=315
print(A) if A>B  else  print(B) if A<B else print('elif')
try:
    no1=int(input('Enter 1st number : '))
    no2=int(input('ENter 2nd nnumber : '))
    no3=int(input('Enter 3rd number : '))
    print(no1,'is greater : ') if no1>no2 and no1>no3 else print(no2,'is greater : ') if no2>no1 and no2>no3 else print(no3,'is greater')if no3>no1 and no3>no2 else print('ALl are equal')
except ValueError:
    print('invalid value : ')
# if you don'tn want to Write anything into the else then :

A=316
B=315
print(A) if A>B  else '' # or else ""

# or we can also do this :
a=3
b=2
 
c= 9 if a>b else 0 # we can also assign a value 
print(c) 

# we can also write it as this 

if a>b :
    c=9
else :
    c=0
