colour='no color'
type='no type'
price=0.0

def update(c,t,p):
    global colour  # to acess the globle variable into the funcation use keyword global 
    colour=c
    global type
    type=t
    global price
    price=p
    print('Full update sucessfully : ')
def updatecolor(c):
    global colour
    colour=c
    print('color update sucessfully : ')
def updatetype(t):
    global type
    type=t 
    print('type eupdate sucessfully : ')   
def updateprice(p):
    global price
    price=p
    print('price eupdate sucessfully : ') 
def display():
    print('color : '+colour+' type : '+type+' price : ',price)
def displaycolor():
    print('color : '+colour)
def displaytype():
    print('Type : '+type)
def displayprice():
    print('price : ',price)

def menu():
    option=0
    while option!=9 :
        option=int(input(' Enter 1 for full update : \n Enter 2 for update color : \n Enter 3 for update type : \n Enter 4 for update price :\n Enter 5 for full display : \n Enter 6 for display color : \n Enter 7 for display type : \n Enter 8 for display price \n Enter 9 for exit :'))
        match option:
            case 1:
                c=input('Enter color ')
                t=input('Enter type ')
                p=float(input('Enter price '))
                update(c,t,p)
            case 2:
                c=input('Enter color ')
                updatecolor(c)
            case 3:
                t=input('Enter type ')
                updatetype(t)
            case 4:
                p=input('Enter price ')
                updateprice(p)
            case 5:
                display()
            case 6:
                displaycolor()
            case 7:
                displaytype()
            case 8:
                displayprice()
            case _:
                print('invalid input : ')
                
menu()
