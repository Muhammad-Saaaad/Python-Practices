import os

# let suppose i want to check which folders are present in the directioory :
# simply i will give the location of that file 

print(os.listdir('Leactures(31-60).py/Os_Modules_paractice.py/mk_folder')) # rembember the order is not maintained 

# if u want to see whats inside all the 100 sub diectiories : 

for i in os.listdir('Leactures(31-60).py/Os_Modules_paractice.py/mk_folder'):
    print(i)  # Prints one sub-Dricteory at a time 
    print(os.listdir(f'Leactures(31-60).py/Os_Modules_paractice.py/mk_folder/{i}')) # prints every files in a current sub-Drictiry 


# To check which drictiory u are writting your current program :
print(os.getcwd()) # output : E:\pythonPractice