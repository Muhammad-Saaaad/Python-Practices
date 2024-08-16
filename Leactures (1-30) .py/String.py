# muntiLine String
name ='''asad  
ali
saad'''

print('my name is ' ,name )

# reverse order using String Slicing
fruit='mango'
print(fruit[:-1]) # it will only print to ' mang '
print(fruit[::-1]) # it will only print like ' ognam '

# Quick Quiz 
nm='Harry'
print(nm[-4:-2])  
# As the number of Character are ' 5 ' so 1st it will do (5-4)=1 and then it will do (5-2)=3 it means that Print from index 1 to less than 3 

# Functions in Strings
d='! my name is saad !!'
# To find the length of String 
print('len()',len(d)) # output : 15 
# To find which value is present how many times 
print('count()',d.count('m'))

# To print in upper case 
print('upper()',d.upper())  # not permenent 
# to print in lower case 
print('lower',d.lower())  # not permenent 
# To split a String at the behave of a letter or a single word :
print('split()',d.split('!')) # not permenent 
# to Strip / cut a special word from the String 
print('strip()',d.strip('!')) # not permenent 
# to replace a character with an other character 
print('replace()',d.replace('my','My'))  # not permenent 
# to make the 1st charcter of a String capitile 
d='my name is saad !!'
print('after some arrangements : ',d)
print('capitalize ',d.capitalize()) # not permenent 
# to make the String be printed into the cernter 
print('center() ',d.center(50)) # here 50 = len(d)+35 where len(d)==15 # not permenent 
# if you want to know wheather the String end with the specfic word or not . this funcation return true or false 
print('endswith() ',d.endswith('!'))
 # We can also check wheather the specfic value is between the String or not using the same funcation 
print('endswith() ', d.endswith("is",0,10)) 
# use this instead
if 'saad' in d:
    print(True)
else:
    print(False)    

print(d)