# A set is collection of unordered elements (means there is no specfic order means u can not take a specfic index from a set )
# In set once u have Written a value that value cannot be changed and also set does not allow a duplicate value 
# if u have 3 written 2 times in a set the it will consider as a single 3 and the other 3 will be remove automatically 
# Set are mutable means u can add remove elements 

# Syntax :
s={1,'ali',3.2,1,True,1}
# print(s[0]) # if u do this then i will give an error as in set there are no indexes 
print(s) #output : {1, 3.2, 'ali'}
# here True won't be printed as true is consider as '1' and 1 will be duplicated here so it won't be printed 

# if u want to make an empty set then
empty={} # if u do this it will take it as dictionary as both dict and set start and ends on {}
print(type(empty),empty)

# Frozan set (Type of a set )
# it is immutable and once u created it u cannot do any changes 
# Syntax:
f_set =frozenset({1,2,3,'wiket'})
print(type(f_set),f_set)
# f_set.add(21) # here it will generate an Attribute error as frozan sets are im-mutable 
# print(f_set)

# to make an empty set do this instead:
empty=set()
print(type(empty),empty)
# you can only get the elements from set by print and by using for loop
for i in s:
    print(i) # no order is mantained in set 

#            Functions in set 

# you can also do this with the set :
my_set = {1, 2, 3, 4}
updated_set = {x * 2 for x in my_set}
print(updated_set)

# to join the 2 sets : 
s1={1,2,3,4,5}
s2={1,2,7,9}
# print(s1+s2) # here it will give error to merg them together we will use .union() method 
print('union() : ',s1.union(s2)) # here s1 values wont't be chnaged 
print('s1 and s2 values : ',s1,s2)
# if u want to take the union of 2 sets and want to change the value os s1 do this :
s1.update(s2) # it will take the union of both and return the value in the s1 
print('update() : ',s1)

s1={1,2,3,4,5}
s2={1,2,7,9}

# intersection and interstion update 
print('intersection() : ',s1.intersection(s2))   # intersection means those values that are common in both sets 
s1.intersection_update(s2) # here it takes the values of s1 and s2 , then take intersection and paste the value into s1
print('intersection update() : ',s1)
# s3={21,23,321,12}
# print(s1.intersection(s2).intersection(s3)) you cant take intersection of 3 sets at a time 

s1={1,2,3,4,5}
s2={1,2,7,9}

# Semetric difference and Semetric difference - update 
 # semectric difference means to take those values are not common 
print('symmetric_difference() ',s1.symmetric_difference(s2))
print(s1,s2)
s1.symmetric_difference_update(s2)
print('symmetric_difference_update() ',s1)

#  Difference and Difference update :
 # it get the elements that are present in the 1st set but not the 2nd set

s1={1,2,3,4,5}
s2={1,2,7,9}
print('difference() : ',s1.difference(s2))
s1.difference_update(s2)
print('difference_update() : ',s1)

# The isdisjoint() method checks if items of given set are present in another set. 
# This method returns False if items are present, else it returns True.

# if a single item is not present it will return true 
print('isdisjoin() : ',s1.isdisjoint(s2))

# isSuperset() check if the give set is the super set of the next set : 
s1={1,2,3,4,5}
s2={1,2,4}

print('issuperset() : ',s1.issuperset(s2))

# isSubset() check if the give set is the sub set of the next set : 
print('issubset() : ',s2.issubset(s1))

# to add a value to a set :
s1.add('ali')
print(s1)

# to remove a value from the set we use 2 funcations :
# remove()/discard()
# when we use remove() , and the value that is being remove is not present in the set 
# it will generate an error while when we use discard() it won't generate error 

s1.remove(5)
print(s1)
# s1.remove(70) generats an error here 
s1.discard(70) # no error is generated 


# pop()
# this will generate a random value from the set and that value from the set 
s1={3,2,7,5,9,12}
item=s1.pop()
print(s1,'\n',item)

# del is a keyword and is use to delete a set completly 
del s1
# print(s1)  # here s1 is deleted so it will not be printed 

#clear() delete all the values from the set but does not delete the set 
s1={1,3,23,12,3}
s1.clear()
print(s1)