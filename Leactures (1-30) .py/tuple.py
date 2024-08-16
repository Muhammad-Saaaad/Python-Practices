# Tuple
 # Tuples are just like list , the only difference is that tuple cannot be changed 

# Syntax :
tup=(1,2,3)
print(type(tup),tup)
# tup[0]=2  # here it will give error as no changes can be made in tuple : 
# if we write this : 

# a tuple as also contain different data types 
tup=(1,2,3,'harry','minion')
print(tup)

tup=(1)
print(type(tup),tup) # here it will conside the 1 written in braces as integer
# to make it tuple we can do this :
tup=(1,)
print(type(tup),tup)
# ok know :
tup=(0,1,2,3)
# we can do slicing in tuple and indexing as well 
print('indexing : ',tup[2])
print('indexing : ',tup[-1])
print('slicing : ',tup[0:2])
# we can also make a new tuple from previous tuple 
tup2=tup[1:3]
print(tup2)

if 2 in tup2:
    print(' yes 2 is present : ')

# Tuples methods :
# 1 : Minuplating Tuples : 
# As tuples are immutable and cannot be change we can only change tuples by making the 
# tuple into a list , do chnages in the list 
# and then again change that list into the tuple :

tup=(1,233,21,5,432,5,52,23,2,12,5,5)
tup=list(tup) 
print(type(tup),tup) # now the taple becomes a list

tup.append('numbers')
print(tup)
tup.pop(0)  # from pop we can remove values by providing the index of that tuple 
print(tup[0])
tup=tuple(tup) 
print(type(tup),tup) 
# So in this way we can muniplicate a tuple indrictely 

# if you want to know the count of a value 
print('count() ',tup.count(5))

# if you want to know the index of a specfic value :
print('index()',tup.index(5)) # it will only show the index of 1st occurance 

# if u want to know that index of a value from the middle of the tuple 
print('indexing with Slicing : ',tup.index(5,7,10)) 
# here it will start form 5 and goes to 10


# we can also make tuple as this method : 
tup='saad','ali','ahmed'
print(type(tup),tup)