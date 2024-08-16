# print('hello there ') # for type casting use '#' 

# Discitonaries 
  # In dictionary there are 2 indxes : 
   # The key index is called 0 and the value index is called 1
    # input values in discitonaries 

City={'houses':20,"building":30,'commerical area':'200 square feet'} 

   # for getting output from discitonaries 

print(City['building']) # output : 30   

   # for changing values 

City['building']=50   

print('Changed value ' , City['building'])

   # for adding new pair value in discitionaries 

City['schools']=5;   

print('new Addation schools : ', City['schools'])

   # Dictionary 
# Dictionaries are ordered collection of data items. They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
# they are use when creating a collection of items in a shop , while creating a database e.t.c 

dic={' name ' : ' saad ' , ' age ' : 18 , ' height ' : '6,3ft'}
 # to acess full dictionary 
print(dic)
# I. Accessing single values : ( THERE ARE 2 WAYS : )  
# The only difference between them is: ( if the key is wrong the 1st one will show error while the 2nd one will show None )
# 1.
print('passing the key : ',dic[' name '])  # rembember the spcaes as well is the keys and values 
# 2. 
print('passing the get() funcation : ',dic.get(' name '))

# or we can do this : 
for i in dic :
    print('passing the get() with the for loop : ',dic.get(i))

# II. Accessing Muntiples values:

# We can print all the values in the dictionary using values() method.

print('Muntiple values : ',dic.values())
val=dic.values()
print(val,type(val)) # it will still remain dictionary 
# or 
for i in dic.values():
    print('using for loop with values()',i)

# III. Accessing Muntiples Keys:

# We can print all the keys in the dictionary using keys() method.

print('Muntiple keys ',dic.keys())
# or
for i in dic.keys():
    print('using key() with for loop : ',i)

# IV. Accessing key-value pairs:

# We can print all the keys-value pairs in the dictionary using items() method.

print('key-value pair : items() ',dic.items())
# or
for i , j in dic.items():
    print('keys : ',i,' values : ',j)

# Function of Dictionary : 

dic1={1:'saad',2:'ali',3:'harry',4:'pg'}
dic2={'age1':18,'age2':19,'age3':25,'age4':18}

# update() is use to merge 2 dictionaries 
 # rembember pass the different keys in the of the dictionaries if u pass the same keys then it will remove the keys in the 1st dictionary 
dic1.update(dic2)
print('update() ',dic1) # output : update()  {1: 'saad', 2: 'ali', 3: 'harry', 4: 'pg', 'age1': 18, 'age2': 19, 'age3': 25, 'age4': 18}

# clear() is use to remove all the key - values from the dictionary 
dic.clear()
print(dic) 
# if u want to make an empty dictionary : 
dic_empty={}
print(dic_empty)

# pop() is use to remove those methods that are passed as a parameter 
dic1.pop(3)
print('pop()',dic1)
# popitem() is use to remove the last item in the dictionary 
dic2.popitem()
print(dic2)

# del is use to delete an dictionary along the memory : 
del dic2
# print(dic2) output : NameError: name 'dic2' is not defined. Did you mean: 'dic'?

# or use can use del to remove a single item 
dic2={1:23,2:32}
del dic2[1]
print(dic2)

# Sorting in dictionary : 
  # sorted method will only return output in the from of list 
dic_name={'Saad':2,'Ali':6,'pg':23,'ha':1}
a=dict(sorted(dic_name.items() , key = lambda  t:t[1]))
print(a)

# for i , j ,k , l in zip(range(5),range(4),range(3),range(4)): # you can pass as much value as u want 
#     print(i,j,k,l)