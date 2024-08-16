# # The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# # reading a single line 
# with open ('new x mode','r') as f :

# # file data :     
# # Saad,56,43,23
# # Ali,21,32,43
# # Ahmed,98,78,89

#     reading=f.readline()
#     print(type(reading),reading) # output : <class 'str'> 56,43,23

# # reading multiple line + difference between read() and readline()
#  # 1. sometimes we need to deal with the data as line by line so we will use readline() with loop 
# with open ('new x mode','r') as f :
#     while True :
#         line=f.readline()
#         if line == '' or not line: # these both are valid 
#             break
#         print(line)

# with open ('new x mode','r') as f :
#     print('new ',f.read())  # here this will print data but 
#     print(f.read())  # not this , as when you get the data from the file the cursor goes to the end and then it does not go back 
#     # if you want the cursor to go back use seek() function  
#     f.seek(0) # the index shows that from which line u want to read the data again 
#     print(f.read()) # now it will print the data form the begining 

# # practice of readline()

# print('practice of readline() \n ')

# with open('new x mode') as f :
#     while True:  
#         line = f.readline()
#         if not line :
#             break
#         m1=line.split(',') # output  : ['56', '43', '23\n']
#         print(f'Marks of student {m1[0]} from English : {m1[1]} ')
#         print(f'Marks of student {m1[0]} from Maths : {m1[2]} ')
#         print(f'Marks of student {m1[0]} from Science : {m1[3]} ')

# print('\n\n')

# # readable() only checks if the file is in readable mod  or not 

# # readlines() 
# #  The readlines() method reads all the lines of the file and returns them as a list of strings.
#   # it returns each line in a single String 

# f= open('new x mode','r')

# lines=f.readlines()   # output : ['Saad,56,43,23\n', 'Ali,21,32,43\n', 'Ahmed,98,78,89']
# for i in lines:
#     m1=i.split(',')
#     print(f'marks of {m1[0]} from English are {m1[1]}')
#     print(f'marks of {m1[0]} from Maths are {m1[2]}')
#     print(f'marks of {m1[0]} from SST are {m1[3]}')
# f.close()


#  # Writelines() 
#  # In python u can only write a String value using write() method . so by using writelines() method u can write iterable object, such as 
#  # a list or a tuple. that have the value in the String only 
#  # The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

# with open('text.txt','w')as f  :
#     lis=['1','2','3']
#     f.writelines(lis)  # output in the text file : 123
#     # if u want to write each index of list on the next line we can do this : 
#     lis=['1\n','2\n','3\n']
#     f.writelines(lis)
#     # or if the list is to big and its difficult to add '\n' to each of the list simply do this : 
#     for i in lis:
#         f.write(i+'\n')


# # The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, 
# # and you can move either forward or backward from the current position.

# with open('new file.txt','r') as f:
#     f.seek(10)
#     print('No Arguments in Read : ',f.read())
#     f.seek(15)
#     print('Argument with read',f.read(5)) # the argument pass in the read() function tells as to read 5 bytes from where the cursor is now.


# # tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location
# #  within the file or for seeking to a specific position relative to the current position. 

# with open('new file.txt') as f :
#     f.seek(7) # suppose i use the seek function in any method now i dont know where is my cursor so i can use tell()

#     print(f.tell())  # output : 7


# truncate() 
# Suppose u open a file  and u want to cut of the size of the file so then we will use truncate function 

with open('new file.txt','w') as f :
    # suppose u want to see the text that is only avalible at the 
    f.truncate(10) 

with open('new file.txt','r') as f :
    f.seek(0)
    # truncate() function then it will delete all the data and put null 
    print('text after truncate : ',f.read()) # here it will show nothing because when u open a file in write or append mode and then perfrom 

# with open('new file.txt','r+') as f:
#     f.truncate(5)  # 
#     print(f.read())