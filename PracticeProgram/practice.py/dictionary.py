cars={'Toyta Supra':0,'Maclearn':0,'Pagani':0,'Lambogeni':0,'Roll Roys':0}
Toyta_Supra=0
Maclearn=0
Pagani=0
Lambogeni=0
Roll_Roys=0
def menu():
    op=0
    while op!=4:
        print('''Enter 1 : Rent a car \nEnter 2 : Delete a car \nEnter 3 : Show Total Rented cars \nEnter 4 : Exit ''')
        op=int(input())
        match op:
            case 1:
                Rent_Car()
            case 2:
                Delete_Car()
            case 3:
                Show_All_Cars()
            case 4:
                print('Exit : ')
            case _:
                print('Invalid input : ')

def Rent_Car():
    for i,j in cars.items():
        print(i,j)
    
    try:

        rc=int(input('Enter 1: Toyta Supra \nENter 2: Maclearn \nEnter 3: Pagani \nEnter 4: Lambogeni \nEnter 5: Roll Roys'))
        
        match rc:

            case 1:
                if Toyta_Supra<5:
                    cars['Toyta Supra']=Toyta_Supra+1
                else:
                    print('Toyta Supra out of Stock : ')
            case 2:
                if Maclearn<5:
                    cars['Maclearn']=Maclearn+1
                else:
                    print('Maclearn out of Stock : ')
            case 3:
                if Pagani<5:
                    cars['Pagani']=Pagani+1
                else:
                    print('Pagani out of Stock : ')
            case 4:
                if Lambogeni<5:
                    cars['Lambogeni']=Lambogeni+1
                else:
                    print('Lambogeni out of Stock : ')
            case 5:
                if Roll_Roys<5:
                    cars['Roll Roys']=Roll_Roys+1
                else:
                    print('Roll Roys out of Stock : ')
            case _:
                print('Invalid input : ')

    except ValueError:
        print('Invalid input : ')


def Delete_Car():
    try:

        rc=int(input('Enter 1: Toyta Supra \nENter 2: Maclearn \nEnter 3: Pagani \nEnter 4: Lambogeni \nEnter 5: Roll Roys'))
        
        match rc:

            case 1:
                if Toyta_Supra>0:
                    cars['Toyta Supra']=Toyta_Supra-1
                else:
                    print('Toyta Supra is not Rented : ')
            case 2:
                if Maclearn>0:
                    cars['Maclearn']=Maclearn-1
                else:
                    print('Maclearn is not Rented : ')
            case 3:
                if Pagani>0:
                    cars['Pagani']=Pagani-1
                else:
                    print('Pagani is not Rented : ')
            case 4:
                if Lambogeni>0:
                    cars['Lambogeni']=Lambogeni-1
                else:
                    print('Lambogeni is not Rented : ')
            case 5:
                if Roll_Roys>0:
                    cars['Roll Roys']=Roll_Roys-1
                else:
                    print('Roll Roys is not Rented : ')
            case _:
                print('Invalid input : ')

    except ValueError:
        print('Invalid input : ')


def Show_All_Cars():
    for i,j in cars.items():
        print('Car : ',i,' Number of Rents : ',j)


menu()