# We have following information on countries and their population (population is in crores),

# Country	Population
# China	     143
# India	     136
# USA	     32
# Pakistan	 21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print 
# that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new 
# dictionary using format shown above in (a). Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
# Solution
dictionary ={'China':143 , 'India' : 136 , 'USA' :32 , 'pakistan' : 21 }
options=0
while options !='exit':
    options=input('Enter print to print : \nEnter add to Add : \nEnter remove to remove : \nEnter query to Perfrom  Query : \nEnter exit to Exit')
    match options :
        case 'print' :
            for key , value in dictionary . items():
                print(f'{key}==>{value}')
            
        case 'add':
            contary_name=input('Enter name of the contary : ')
            if contary_name in dictionary.keys():
                print('It exists : ')
            else :
                pop=int(input('Enter the population of the contary : '))
                dictionary[contary_name] = pop
                print(f'{contary_name}==>{pop}')
        case 'remove':
            contary_name=input('Enter contary name : ')
            if contary_name in dictionary.keys():
                del dictionary[contary_name]
                for key , value in dictionary . items():
                    print(f'{key}==>{value}')
            else :
                print('Contary does not exist : ')
        case 'query':
            contary_name=input('Enter the name of contary on which you wants to perform query : ')
            print(f'{contary_name}==>{dictionary[contary_name]}')
        case 'exit':
            print('Exit : ')
        case _:
            print('Invalid input : ')


# You are given following list of stocks and their prices in last 3 days,

# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will 
# append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will 
# add tata ==> [560] to the dictionary of stocks.
# Solution
Stock={'info':[600,630,620],'ril':[1430,1490,1567],'mtl':[234,180,160]}
options=0
while options !='exit':
    options=input('Enter print to print : \nEnter add to Add : \nEnter exit to Exit')

    match options:
        case 'print':
            for key , value in Stock.items():
                print(f'{key} ==> {value}')
        case 'add':
            ticker=input('Enter ticker : ')
            price=int(input('Enter the price : '))
            if ticker in Stock.keys():
                Stock[ticker].append(price)
            else :
                Stock[ticker]=[price]
        case 'exit':
            print('exit : ')

# Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference
#  and diameter. You should get these values in your main program by calling circle_calc function and then print them

def circle_calc():
    radius = float(input('Enter a value for the radius : '))
    options =input('''
Enter area to calculate area of the circle
Enter cmf to calculate circumference of the circle 
Enter diameter to  find the diameter of the circle ''')
    match options:
        case 'area':
            print('area of the circle = ', 3.1416*radius*radius)
        case 'cmf':
            print('circumference of the circle is = ',2*3.1416*radius)
        case 'diameter':
            print('Diameter of the circle = ',2*radius)
        case _:
            print('Invalid Input : ')

circle_calc()
