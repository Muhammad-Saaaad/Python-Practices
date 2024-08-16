# Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. 
# It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading,
# 'w' for writing, or 'a' for appending.
# file only accept the data in String form 

# Here's an example of how to open a file for reading:

f=open('text.txt','r')
read=f.read()
print(f.read()) # if we do this then nothing will be printed because you can only read once u open a file but this is also valid 
print(type(read),read) # output : <class 'str'> hi there , 
f.close()

# By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.

# Modes : 
 # 1 . read (r): This mode opens the file for reading only and gives an error if the file does not exist. 
 #     This is the default mode if no mode is passed as a parameter.
f=open('text.txt') # here by default it have the read mode enable
read=f.read()
print(read)
f.close() # you always need to close the file once you opens a file 

 # 2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
 #   if the file already contain some data and u write into the file the previous data will be removed automatically 

f=open('new file','w') # create a new file as the '  new file ' does not existed 

f=open('text.txt','w')
writing=input('Enter something to b input into the file : ') # here we are taking input from user and then writing that input into that file 
f.write('\n'+writing) # if  u need to write data into  the next line then use '\n' with the concatetation mark . do not put the , sign 
print('Writing into the file is sucessfully done : ')
f.close()

 # 3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
 #  it is use to write into the file without removing any data from the file 

f= open('text.txt','a')
f.write('appending a file : ')
# here as both file have the same variable . if u don't close a file explicitliy the python garbage collector will close it automatically 
# but rembemeber it is important to close the file explicitly 
f.close()
f=open('text.txt','r')
print(f.read())# output : my name is unknow pg appending a file 
f.close()

  # 4. create (x): This mode creates a file and gives an error if the file already exists.

f=open('new x mode','x')
print('file created : ')
f.close()


 # 5. text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files.
 # t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. 
 # The default mode is 'r' (open for reading text, synonym of 'rt' ).

# 6 . binary (b): used to handle binary files (images, pdfs, etc).


# Alternatively, you can use the with statement to automatically close the file after you are done with it.

with open ('new file','w') as f :
  f.write('something in the file')  # when we do not add extentation , then its depend upon the type of data written in the file 
  # if the data is in the text , it will consider it as text file if the data is in binary it will consider it in the binary form  
with open('new file.txt','r') as g:
  print(g.read())
    