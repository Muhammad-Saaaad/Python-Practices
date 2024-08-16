class duplicate(Exception):
    pass

Id =0
company='no company'
model=0
color='no color'
price=0.0

data=[]

def menu():
    option=0
    while option !=7:
        print ('''Your options are:
1.	Enter 1 to load data from storage
2.	Enter 2 to save data in storage
3.	Enter 3 add new mobile
4.	Enter 4 update a mobile
5.	Enter 5 sell a mobile
6.  Enter 6 to Show all mobiles
7.	Enter 7 exit''')
        try:
            option = int(input())
            match option:
                case 1:
                    load_data()
                case 2:
                    save_data()           
                case 3:
                    add_new_mobile()
                    print('mobile added : ')
                case 4:
                    update_a_mobile()
                    print('mobile updated : ')
                case 6 :
                    show_data()
                case 7 :
                    print('Exit :')
        except ValueError:
            print('Invalid input : ')


def load_data():
    global data
    try:
        with open ('new file.txt','r') as f :
            lines = f.readlines()
            for line in lines :
                for index in data :
                    if line[0] == index[0]:
                        
                        pass   
                    data.append(line)
        print('data loaded sucessfully : ')
    except :
        print('Some error occure : ')

def save_data():
    global data
    with open ('new file.txt','w') as f :
       for index in data:
            for j in index :
                if type(j) == int or type(j) == float:
                    f.write(str(j)+'\t')
                else :
                    f.write(j+'\t')
            f.write('\n')
    print('data saved sucessfully : ')
        
def add_new_mobile():
    global data
    try:
        Id=int(input('Enter id : '))
               
        if len(data) > 0:
            for index in data:
                if index[0] ==Id : 
                    raise duplicate('duplicate')
            
        company=input('Enter name of company : ')
        model=int(input('Enter model of mobile : '))
        color=input('Enter color of mobile : ')
        price=float(input('Enter price of mobile : '))
        f=[Id,company,model,color,price]
        data.append(f) 
    
    except ValueError:
        print('invalid input : ')
    except duplicate:
        print('No duplicate Id : ')

def update_a_mobile():
    global data
    try:
        Id=int(input('Enter id for data updating : '))
        update=0
        index_no=-1
        if len(data) != 0 :
            for index in data :
                index_no+=1
                if Id == index[0]:
                    update=1
                    Id=int(input('Enter id : '))
                    company=input('Enter name of company : ')
                    model=int(input('Enter model of mobile : '))
                    color=input('Enter color of mobile : ')
                    price=float(input('Enter price of mobile : '))
                    f=[Id,company,model,color,price]
                    data[index_no]=f
            print('Id is not present : ') if update == 0 else print('Data updated sucessfully : ')
        else : 
            print('No data avalible to update at this time : ')

                    
    except ValueError:
        print('invalid input : ')

def show_data():
    for d in data :
        print(d)
menu() # function call

# string='1234'   # if there is a value that have the different data type : 
# li=list(string)
# li.append(7)
# f = open('new file.txt','w')
# for i in li:
#     if type(i) == int:
#       f.write(str(i))
#     else :
#       f.write(i)
# f.close()

# f = open('new file.txt','r')
# print(f.read())
# f.close()


# listing=[]
# def take_data():
#     f=[]
#     try:
#         Id=int(input('ENter your id : '))
#         name=input('Enter name : ')
#         degree=input('ENter your degree : ')
#         f.append(Id)
#         f.append(name)
#         f.append(degree)
#     except ValueError:
#         print('Invalid input :')

#     return f

# def save_data():
#     with open ('text.txt','a') as f :
#         f.write()

# admission=int(input('Enter number of admission u want : '))
# for i in range(admission):
#     listing.append(take_data())
#     print(listing)
#     # write
# with open ('text.txt','a') as f :
#     for index in listing:
#         for j in index :
#             if type(j) == int :
#                 f.write(str(j)+'\t')
#             else :
#                 f.write(j+'\t')
#         f.write('\n')
# with open ('text.txt','r') as f :
#     reading=f.readlines()
#     for line in reading:
#         print(line )