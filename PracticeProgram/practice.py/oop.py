buses=[['Islamabad', 'Karachi' , '7:00 AM to 9:00AM'] , ['Islamabad','Multan','8:00 AM to 10:00 AM'],['Islamabad','Lahour','10:00 AM to 12:00 PM']]
seats=[[3],[3],[3]]
class Bus_Booking:

    B1=0
    B2=0
    B3=0

    def menu(self):
        option =0
        while option !=5 :
            option=int(input('''
Enter 1 to Book a Bus : 
Enter 2 to Cancle a Bus :
Enter 3 to Search by Deparature and Destination : 
Enter 4 to view all buses : 
Enter 5 to Exit menu : '''))
            match option : 
                case 1 :
                    self.Book_Bus()  #  to call a function into another function in a class use self keyword
                case 2:
                    self.bus_cancle()
                case 3 :
                    self.search_Bus()
                case 4 :
                    self.view_all_Buses()
                case 5 :
                    print('Exit : ')
                case _ :
                    print('Invalid input : ')

    
    def Book_Bus(self):
        try:
            for i in range(3):
                print(f'\nEnter {i+1} to  Book Bus no {i+1}')
                for j in range(3):
                    print(buses[i][j])
            booking=int(input())
        except ValueError:
            print('Invalid input :::::')
            return None

        if booking == 1:
            # global B1 #Do not use global keyword as it refers to the variable that is not present in any function or class but present globally
            if seats[0][0] > 0 :
                seats[0][0]-=1
                print('Booking completed ::')
                Bus_Booking.B1+=1 # instead do this 
            else:
                print('All seats are Booked : ')
        elif booking == 2:
            if seats[1][0] > 0 :
                seats[1][0]-=1
                print('Booking completed :: ')
                Bus_Booking.B2+=1 
            else:
                print('All seats are Booked : ')
        elif booking == 3: 
            if seats[2][0] >0 :
                seats[2][0]-=1
                print('Booking completed :: ')
                Bus_Booking.B3+=1
            else:                                   # do this in cancilation as well 
                print('All seats are Booked : ')


    def bus_cancle(self):
        try:
            for i in range(3):
                print(f'\nEnter {i+1} to  cancle Bus no {i+1}')
                for j in range(3):
                    print(buses[i][j])
            Cancling=int(input())
        except ValueError:
            print('Invalid Input : ')
            return  None

        if Cancling == 1:
            # global B1 #Do not use global keyword as it refers to the variable that is not present in any function or class but present globally
            if seats[0][0] <3  and Bus_Booking.B1 >0 :
                seats[0][0]+=1
                print('Seat Cancled ::')
                Bus_Booking.B1-=1 # instead do this 
            else:
                print('No Seat was booked by you : ')
        elif Cancling == 2:
            if seats[1][0] < 3 and  Bus_Booking.B2 >0 :
                seats[1][0]+=1
                print('Seat cancled :: ')
                Bus_Booking.B2-=1 
            else:
                print('No Seat was booked by you : ')
        elif Cancling == 3:
            if seats[2][0] < 3 and Bus_Booking > 0:
                seats[2][0]+=1
                print('Seat cancled :: ')
                Bus_Booking.B-=1
            else:
                print('No Seat was booked by you : ')
    def search_Bus(self):
        departure=input('Enter departure : ')
        Distination=input('Enter the Distination : ')
        find=False
        for i in range(3):
            if buses[i][0].capitalize() == departure.capitalize() and buses[i][1].capitalize() == Distination.capitalize():
                print(buses[i])
                find=True
        if find==False:
            print('No bus was found : ')

    def view_all_Buses(self):
        for i in range(3):
            for j in  range(3):
                print(buses[i][j],end=' ')
            print('\n')
                

obj1=Bus_Booking()
obj1.menu()