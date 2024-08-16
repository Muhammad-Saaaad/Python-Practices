# List 
 # In python , list is just like an array and list can also hold a different datatypes at the same time 

_list=[1,2,3,'saad']
print(_list[3])

# Also we can check wheather the element is in the list or not by using the in keyword  ....
if 1 in _list:
    print('yes')
# the same thing can be apply for String 
if 'a' in 'saad':
    print('yes')

print(_list,end=' ')  # most of the method of String can also b apply on list 
print(_list)    

print(_list[:2]) # Slicing of list 

# List compresentation :
 # list compresentation are use to create a new list from other iterateable like list,String,tuple and disc e.t.c

# Syntax : 
#  list compresentation name = [any expression for variable in iterateable if condation ]
# Or 
#  list compresentation name = [any expression for variable in iterateable]
# Or
#  list compresentation name = [any expression if condation with else (else must ) for variable in iterateable ]
#  EX:

numbers=[23,27,54,34,12,25,245,231,99,22,234]
print('numbers list : ',numbers)

modify_even_numbers=[i*i for i in numbers if i%2==0]
print('modify even numbers : ',modify_even_numbers)

evennumbers=[i if i%2==0 else -1 for i in numbers ]
print('Even numbers list :',evennumbers)

# List Funcation : 

 # To add a value to a list permentally 
l=[2,33,1,432,21,2]
a=82
l.append(a) # here no matter how many values you add. all the values will be saved in an one index 
print(l)

# To sort a value , it will also have a permenent effect on it 
l.sort()   # if the values are in String then the sorting will be done by the length on String 
print(l) 
l.sort(reverse=True)
print(l)

# To know the idex of a particular value 
print('num of indexes',l.index(2))

# To count the number of specfic values that are present in the list
print('num of counts ',l.count(2))

# do not do this : 
# l=[432, 82, 33, 21, 2, 2, 1]
# b=l           # here they both share the same reference and the changing in one cause the chnaging in other variable as well
# b[0]=0
# print(b)   # output : [0, 82, 33, 21, 2, 2, 1]
# print(l)   # output : [0, 82, 33, 21, 2, 2, 1]  

# It will change the values in the original list 
# b=l   
# b=[0]      # as this is python , so if any new value enters the previous value is removed 
# print(l)  #   output :    [432, 82, 33, 21, 2, 2, 1]
# print(b)  # output :   [0]
# but here it won't 

# to copy the list to an other variable use this

b=l.copy()
b[0]=0
print(l,'\n',b) # here u won't get any issue using copy function

# to add a new value to a specfic index without removing any other value use this function :

l.insert(1,899)
print(l)

# to add a list with another list use this function : 

m=[900,1100,1500]
l.extend(m)
print(l)  # output : [432, 899, 82, 33, 21, 2, 2, 1, 900, 1100, 1500]
print(m)  # output : [900,1100,1500]

# to add 2 list with each other without interfaring any of them use 
# Concatetation(+):
k=l+m
print(k)

k.pop(0)  # from pop we can remove values by providing the index of that list 
print(k)

# to convert a list into int 
  # first convert the list into String using the join and a seprator 
  # and then convert the String into the int 
l=[1,2,3,4,5]
joined_string = ''.join(str(x) for x in l) #'' is a seprator 
print(int(joined_string))

# to convert a Sentence of String into a list of words  :
sentence='Hello there'
li=sentence.split(' ') # output : ['Hello', 'there', '']
print(li)

# to convert a Sentence of String into a list of characters  :
li=list(sentence)
print(li)