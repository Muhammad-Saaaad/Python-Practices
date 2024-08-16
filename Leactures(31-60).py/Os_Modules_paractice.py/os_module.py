# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to
# perform a wide variety of tasks,  like creating files and directories, management of files and directories, input, output, environment
# variables, process management, etc. 

import os 

# os.mkdir('d:\ file from os ')  # we can simply provide the location at which we want to create the folder/directiory and 
# the os will make that folder/directiory for us 
if not os.path.exists('Leactures(31-60).py/Os_Modules_paractice.py/mk_folder'): # means that if the data directiory does not exist then create the dictiory : 
    os.mkdir('Leactures(31-60).py/Os_Modules_paractice.py/mk_folder')
# means that to create a directiory named mk_folder in the specfic location 

# Now if i want to create sub folders into the mk_folder directiory then i will do this

for i in range (100):
    os.mkdir(f'Leactures(31-60).py/Os_Modules_paractice.py/mk_folder/data {i+1}') 
# In this way i can create 100 folder in a blink of an eye named data 
