from random import choice

Title='Snake Water Gun '
print(Title.center(100))

matrix=[['Draw','Win','Lose'],['Lose','Draw','Win'],['Win','Lose','Draw']]

def game():
    play=1
    while play!=0:
        try:
            print('''Enter 1 : Gun 
Enter 0 : Water 
Enter -1 : Snake \n''')
            # choice Start
            user=int(input('Enter your choice :\t'))
            if user >1 or user <-1 : 
                raise ValueError
            computer=choice([-1,0,1])

            if computer == -1 :
                print('Computer choice :\t','Snake')
            elif computer == 0 : 
                print('Computer choice :\t','Water')
            elif computer == 1 :
                print('Computer choice :\t','Gun')



            if user == -1 and computer == -1:
                print(matrix[0][0])
            elif user ==-1 and computer ==0:
                print(matrix[0][1])
            elif user == -1 and computer == 1 :
                print(matrix[0][2])
            elif user == 0 and computer == -1 :
                print(matrix[1][0])
            elif user == 0 and computer == 0 :
                print(matrix[1][1])
            elif user == 0 and computer == 1 :
                print(matrix[1][2])
            elif user == 1 and computer == -1 :
                print(matrix[2][0])
            elif user == 1 and computer == 0 :
                print(matrix[2][1])
            elif user == 1 and computer == 1 :
                print(matrix[2][2])
            

        except ValueError:
            print('\ninvalid input :\n')



        play=int(input('\nEnter 1 to play again \nEnter 0 to Exit Game : \n'))
game()