# Question 1: Divide and Catch
try:
    no1=float(input('Enter no1 : '))
    no2=float(input('Enter no2 : '))    
    print(f'Division of both number is : {no1/no2}')
except ZeroDivisionError:
    print('number cannot  be divisiable by zero : ')

# Suppose we want to do Exception handling in this program : 

p_b={}
condations='''Enter 1 : Add a new contact to the phone book
Enter 2 :Update an existing contact's phone number.
Enter 3 :Delete a contact from the phone book.
Enter 4 :Search for a contact by name and display their phone number.
Enter 5 :Display the entire phone book directory.
Enter 6 :Exit.'''
def phone_book():
    op=0
    while op!=6:
        print(condations)
        op=int(input())
        match op:
            case 1:
                add_new_contract()
            case 2:
                update_contacct()
            case 3:
                delete_contact()
            case 4:
                search_contact()
            case 5:
                display_full_Book()
            case 6:
                print('Exit : ')
            case _:
                print('Invalid input : ')


def add_new_contract():
    try:
        name=input('\nEnter name of your contract : \n')
        phone_no=int(input('Enter your phone number : \n'))
        p_b[name]=phone_no
        print('Contact Added : \n')
    except ValueError:
        print('Enter the contact no in numbers : \n   Contact not Added')

def update_contacct():
    try:
        name=input('\nEnter name of your contract which u want to update : \n')
        phone_no=int(input('Enter your new phone number : \n'))
        p_b[name]=phone_no
        print('Contact updated : \n')
    except ValueError:
        print('Enter the contact no in numbers : \n   Contact not Added')
    
def delete_contact():
    try:
        name=input('\nEnter name of your contract which you want to delete : \n')
        del p_b[name]
    except:
        print('Name is not present : ')

def search_contact():
    try:
        name=input('\nEnter your name... \n')
        print(name ,'  ', p_b[name],'\n')
    except:
        print('Name is not present : ')

def display_full_Book():
    for names,contacts in p_b.items():
        print(names,'  ',contacts,'\n')

phone_book()
