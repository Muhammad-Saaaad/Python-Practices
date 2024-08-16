hour=int(input('Enter hour : '))
minuts=int(input('Enter minutes : '))
seconds=int(input('Enter Seconds : '))
duration=input('Enter the time duration : ')

if(duration=='am' and hour>=5 and hour <11):
    print('good Morning sir : ') 
elif((duration=='am'or duration=='pm') and (hour>=11 and hour<4) ) :
    print('Good Afternoon Sir : ')   
elif(duration=='pm' and hour>=4 and hour <=8):
    print('Good Evening Sir ')
elif((duration=='pm' or duration == 'am') and (hour>8 and hour<5)):
    print('Good night Sir : ')