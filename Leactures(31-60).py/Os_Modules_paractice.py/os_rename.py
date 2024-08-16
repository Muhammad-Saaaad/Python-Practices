import os

# we can also rename all the sub-directiories / files : 

for i in range(100):
    # 1st provide the source and then provide the distination 
    os.rename(f'Leactures(31-60).py/Os_Modules_paractice.py/mk_folder/data {i+1}' , f'Leactures(31-60).py/Os_Modules_paractice.py/mk_folder/Sub_Directiory {i+1}')