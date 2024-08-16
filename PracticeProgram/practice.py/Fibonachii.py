def fibo(num):
    num3=[0,1]
    if num==0:
        return None
    elif num==1:
        return 0
    elif num==2:
        return num3
    else:
        for i in range (num):
            if len(num3) != num :
                num3.append(num3[i]+num3[i+1])
        return num3

try: 
    number=int(input('Enter a number to find fibonachii series : '))
    print(fibo(number))
except ValueError:
    print('Invalid value : ')